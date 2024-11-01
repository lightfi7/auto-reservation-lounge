from pydantic import BaseModel, Field


class Emulator(BaseModel):
    name: str
    description: str
    server_url: str
    usable_num: int | None = Field(default=2)
    status: int | None = Field(default=0)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "Local emulator",
                "description": "This is the local emulator",
                "server_url": "http://127.0.0.1:4723",
            }
        }