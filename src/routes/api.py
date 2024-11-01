from fastapi import APIRouter
from src.endpoints import tasks
router = APIRouter()
router.include_router(tasks.router)