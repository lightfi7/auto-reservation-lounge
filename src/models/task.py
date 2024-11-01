import uuid

from pydantic import BaseModel, Field, validator


class Task(BaseModel):
    user_id: str
    action: str
    log: str
    success: int

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "",
                "action": "",
                "success": 1,
                "log": "",
            }
        }