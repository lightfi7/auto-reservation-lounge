from typing import Optional
from typing_extensions import Annotated

from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Task(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    user_id: str
    params: list[str] = []
    success: bool | None = Field(default=False)
    base64_image: str | None = Field(default="")
    log: str | None = Field(default="")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "",
                "params": ['Даллес@Вашингтон, США', 'Turkish Airlines Lounge@Зал B', 'John@Doe'],
            }
        }