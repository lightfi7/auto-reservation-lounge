# Project Overview

This document provides a comprehensive guide for setting up and running a project that utilizes MongoDB, Python, Node.js, Appium, and Android Studio. It includes instructions for installation, usage, and details about the API endpoints and data models employed in the project.

## Prerequisites

Before you begin, ensure that you have the following software installed:

- **MongoDB**: NoSQL database for storing application data.
- **Python**: Programming language used for backend development.
- **Node.js**: JavaScript runtime for building scalable network applications.
- **Appium**: Open-source tool for automating mobile applications.
- **Android Studio**: Integrated development environment (IDE) for Android app development.

## Installation Instructions

To set up the project, follow these steps:

1. **Install Required Packages**:
   Run the following command to install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   Start the application by executing:
   ```bash
   python main.py
   ```

## API Endpoints

The application exposes several RESTful API endpoints for managing emulators and tasks.

### Emulator Endpoints

- **Get All Emulators**:  
  `GET {HOST:PORT}/emulators`

- **Get Emulator by ID**:  
  `GET {HOST:PORT}/emulators/{emulator_id}`

- **Create New Emulator**:  
  `POST {HOST:PORT}/emulators`

- **Update Existing Emulator**:  
  `PUT {HOST:PORT}/emulators/{emulator_id}`

- **Delete Emulator**:  
  `DELETE {HOST:PORT}/emulators/{emulator_id}`

### Task Endpoints

- **Get All Tasks**:  
  `GET {HOST:PORT}/tasks`

- **Get Task by ID**:  
  `GET {HOST:PORT}/tasks/{task_id}`

- **Create New Task**:  
  `POST {HOST:PORT}/tasks`

- **Update Existing Task**:  
  `PUT {HOST:PORT}/tasks/{task_id}`

- **Delete Task**:  
  `DELETE {HOST:PORT}/tasks/{task_id}`

## Data Models

### Emulator Model

The `Emulator` model represents an emulator instance in the system.

```python
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
                "name": "Local Emulator",
                "description": "This is the local emulator",
                "server_url": "http://127.0.0.1:4723",
                "udid": "emulator-5556",
            }
        }
```

### Task Model

The `Task` model encapsulates a task associated with a user.

```python
class Task(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
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
                "params": "['Dulles@Washington, USA', 'Turkish Airlines Lounge@Gate B', 'John@Doe']",
            }
        }
```

## Appium Integration

To interact with mobile devices using Appium, you can list connected devices using the following command:

```bash
adb devices
```

This will display a list of attached devices, for example:

```
List of devices attached
emulator-5556   device
emulator-5558   device
```

## Conclusion

This guide provides a structured approach to setting up and running your project. By following these instructions, you will be able to efficiently manage emulators and tasks within your application. For further assistance or advanced configurations, please refer to the official documentation of each technology used in this project.