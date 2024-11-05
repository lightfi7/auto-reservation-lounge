# Prerequest
mongodb
python
nodejs
appium
android studio

# How to run
#### <code> pip install -r requirements  </code>
#### <code> python main.py  </code>




# Endpoints
### Emulator endpoint
    GET {HOST:PORT}/emulators
    GET {HOST:PORT}/emulators/{emulator_id}
    POST {HOST:PORT}/emulators
    PUT {HOST:PORT}/emulators/{emulator_id}
    DELETE {HOST:PORT}/emulators/{emulator_id}
### Task endpoint
    GET {HOST:PORT}/tasks
    GET {HOST:PORT}/tasks/{task_id}
    POST {HOST:PORT}/tasks
    PUT {HOST:PORT}/tasks/{task_id}
    DELETE {HOST:PORT}/tasks/{task_id}

# Models
### Emulator

    class Emulator(BaseModel):
        id: Optional[PyObjectId] = Field(alias="_id", default=None),
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

### Task

    class Task(BaseModel):
        id: Optional[PyObjectId] = Field(alias="_id", default=None),
        user_id: str
        params: str
        success: bool | None = Field(default=False)
        base64_image: str | None = Field(default="")
        log: str | None = Field(default="")
    
        class Config:
            populate_by_name = True
            json_schema_extra = {
                "example": {
                    "user_id": "",
                    "params": "['Даллес@Вашингтон, США', 'Turkish Airlines Lounge@Зал B', 'John@Doe']",
                }
            }



# Appium
    