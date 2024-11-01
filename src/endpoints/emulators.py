from fastapi import APIRouter, Body, Request, status, HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from src.models.emulator import Emulator

router = APIRouter(prefix="/emulators", tags=["Emulators"])

@router.get("/", response_model=List[Emulator])
def get_tasks(request: Request) -> List[Emulator]:
    return request.app.database["emulators"].find()

@router.get("/{emulator_id}", response_model=Emulator)
def get_task(request: Request, emulator_id: str) ->Emulator:
    return request.app.database["emulators"].find_one({"_id": emulator_id})

@router.post("/", response_model=Emulator)
def create_task(request: Request, emulator: Emulator):
    emulator = jsonable_encoder(emulator)
    new_emulator = request.app.database["emulators"].insert_one(emulator)
    created_emulator = request.app.database["emulators"].find_one({"_id": new_emulator.inserted_id})
    return created_emulator

@router.put("/{emulator_id}", response_model=Emulator)
def update_task(request: Request, emulator_id: str, emulator: Emulator):
    emulator = {k: v for k, v in emulator.dict().items() if v is not None}
    if len(emulator) != 0:
        updated_result = request.app.database["emulators"].update_one({"_id": emulator_id}, {"$set": emulator})
        if updated_result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Emulator not found")
    if existing_task := request.app.database["emulators"].find_one({"_id": emulator_id}) is not None:
        return existing_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Emulator not found")

@router.delete("/{emulator_id}", response_model=Emulator)
def delete_task(request: Request, emulator_id: str):
    deleted_emulator = request.app.database["emulators"].delete_one({"_id": emulator_id})
    if deleted_emulator.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return f"Emulator with ID {emulator_id} deleted"

