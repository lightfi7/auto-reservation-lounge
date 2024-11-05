from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
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