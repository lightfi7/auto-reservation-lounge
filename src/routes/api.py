from fastapi import APIRouter
from src.endpoints import tasks, emulators

router = APIRouter()
router.include_router(tasks.router)
router.include_router(emulators.router)
