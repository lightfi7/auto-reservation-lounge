# Project Overview

This document provides a comprehensive guide for setting up and running a project that utilizes MongoDB, Python, Node.js, Appium, and Android Studio. It includes instructions for installation, usage, and details about the API endpoints and data models employed in the project.

## Prerequisites

Before you begin, ensure that you have the following software installed:

- **MongoDB**: NoSQL database for storing application data.
- **Python**: Programming language used for backend development.
- **Node.js**: JavaScript runtime for building scalable network applications.
- **Appium**: Open-source tool for automating mobile applications.
- **Android Studio**: Integrated development environment (IDE) for Android app development.
- **Java Development Kit (JDK)**: Ensure you have JDK installed as Appium requires it to function properly. You can download it from the official Oracle website or adopt OpenJDK.



## Step-by-Step Installation

### 1. Install Android Studio

- **Download Android Studio**: Go to the [official Android Studio website](https://developer.android.com/studio) and download the installer for your operating system.
  
- **Run the Installer**: Follow the installation wizard. Choose the standard installation option, and accept any prompts regarding SDK components.

- **Set Up SDK**:
  - Open Android Studio.
  - Go to **More Actions > SDK Manager**.
  - In the **SDK Platforms** tab, select the Android version you want to use and click **Apply** to install it.
  - In the **SDK Tools** tab, ensure that essential tools like `Android SDK Build-Tools`, `Android Emulator`, and `Android SDK Platform-Tools` are installed.

### 2. Install Appium

- **Using Command Line**:
  - Open Command Prompt as Administrator.
  - Run the following command to install Appium globally:
    ```bash
    npm install -g appium
    ```
  - To check if Appium is installed correctly, run:
    ```bash
    appium --version
    ```

- **Install Appium Driver for Android**:
  - Run this command to install the UiAutomator2 driver, which is necessary for Android automation:
    ```bash
    appium driver install uiautomator2
    ```

### 3. Configure Environment Variables

- Set up environment variables for Java and Android SDK:
  - For Windows:
    - Right-click on **This PC > Properties > Advanced system settings > Environment Variables**.
    - Add a new variable `JAVA_HOME` pointing to your JDK installation path (e.g., `C:\Program Files\Java\jdk-21`).
    - Add another variable `ANDROID_HOME` pointing to your Android SDK location (e.g., `C:\Users\<YourUsername>\AppData\Local\Android\Sdk`).
    - Update the `Path` variable by adding `%JAVA_HOME%\bin` and `%ANDROID_HOME%\platform-tools`.

### 4. Create Bluestack Emulator and Settings
  - Launch BlueStacks on your computer.
  - Click on the hamburger menu (three horizontal lines) or the gear icon in the top right corner to open the Settings menu.
  - In the Settings menu, navigate to the Advanced section.
  - Find the option labeled Enable Android Debug Bridge (ADB) and toggle it on. Ensure that BlueStacks remains open while you make this change.
  - Open a command prompt or terminal window on your computer.
  - Navigate to the directory where adb.exe is located, typically found in:
    ```
    C:\Users\<YourUsername>\AppData\Local\Android\Sdk\platform-tools
    ```
  - You can check if BlueStacks is connected by running:
    ```bash
    adb devices
    ```
  - This should list your BlueStacks instance as a connected device.
  - Install the Lounge app on your emulator and log in.
  - After log in, you should keep the Lounge app at the first page.

### 5. Start Appium Server

- You can start the Appium server via Command Prompt by simply typing:
  ```bash
  appium
  ```
- Alternatively, you can use the Appium Desktop client for a GUI option.

### 6. Verify Installation

- To verify that everything is set up correctly, you can run a simple test script using Appium with your emulator running.


# How to setup the project


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
