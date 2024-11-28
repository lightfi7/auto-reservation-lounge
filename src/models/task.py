import uuid

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: str = Field(default=str(uuid.uuid4().hex))
    user_id: str
    params: list[str] = []
    success: bool | None = Field(default=False)
    base64_image: str | None = Field(default="")
    log: str | None = Field(default="")

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "",
                "params": ['Даллес@Вашингтон, США', 'Turkish Airlines Lounge@Зал B', 'John@Doe'],
            }
        }