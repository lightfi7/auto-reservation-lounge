import uuid

from pydantic import BaseModel, Field


class Emulator(BaseModel):
    id: str = Field(default=str(uuid.uuid4().hex))
    name: str
    description: str
    server_url: str
    udid: str
    usable_num: int | None = Field(default=2)
    status: int | None = Field(default=0)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Local emulator",
                "description": "This is the local emulator",
                "server_url": "http://127.0.0.1:4723",
                "udid": "emulator-5556",
            }
        }