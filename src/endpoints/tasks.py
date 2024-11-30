import uuid
from typing import List
from fastapi import APIRouter, Request, status, HTTPException, BackgroundTasks
from fastapi.encoders import jsonable_encoder

from src.models.task import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[Task])
def get_tasks(request: Request) -> List[Task]:
    return request.app.database["tasks"].find()


@router.get("/{task_id}", response_model=Task)
def get_task(request: Request, task_id: str) -> Task:
    return request.app.database["tasks"].find_one({"id": task_id})


@router.post("/", response_model=Task)
def create_task(request: Request, task: Task, background_tasks: BackgroundTasks):
    task = jsonable_encoder(task)
    task['id'] = str(uuid.uuid4())
    new_task = request.app.database["tasks"].insert_one(task)
    created_task = request.app.database["tasks"].find_one({"_id": new_task.inserted_id})
    return created_task


@router.put("/{task_id}", response_model=Task)
def update_task(request: Request, task_id: str, task: Task):
    task = {k: v for k, v in task.dict().items() if v is not None}
    if len(task) != 0:
        updated_result = request.app.database["tasks"].update_one({"id": task_id}, {"$set": task})
        if updated_result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    existing_task = request.app.database["tasks"].find_one({"id": task_id})
    if existing_task is not None:
        return existing_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.delete("/{task_id}", response_model=Task)
def delete_task(request: Request, task_id: str):
    deleted_task = request.app.database["tasks"].delete_one({"id": task_id})
    if deleted_task.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return f"Task with ID {task_id} deleted"
