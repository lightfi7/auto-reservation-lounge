from pydantic import BaseModel, Field


class Task(BaseModel):
    user_id: str
    action: str
    success: bool | None = Field(default=False)
    log: str | None = Field(default="")
    result: str | None = Field(default="")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "",
                "action": "",
            }
        }