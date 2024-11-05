from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Emulator(BaseModel):
    id: UUID = Field(default_factory=uuid4)
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