import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class Emulator(BaseModel):
    id: str = Field(default=str(uuid.uuid4().hex))
    name: str
    description: str
    server: str
    udid: str
    usable_num: int | None = Field(default=2)
    status: int | None = Field(default=2)
    date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Local emulator",
                "description": "This is the local emulator",
                "server": "127.0.0.1",
                "udid": "emulator-5556",
                "date": "2024-02-13 08:20:30"
            }
        }