import uuid

from pydantic import BaseModel, Field, validator


class Task(BaseModel):
    id: str=Field(default_factory=uuid.uuid4, alias='id')
    user_id: str
    action: str
    log: str
    success: int

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "<KEY>",
                "action": "<ACTION>",
                "success": 1,
                "log": "Task created",
            }
        }