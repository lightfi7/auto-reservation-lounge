from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import schedule
import time
from pymongo import MongoClient

from src.bot.auto import award

mongo_client = MongoClient('mongodb://127.0.0.1:27017/')
database = mongo_client['lounge']
print("Connected to MongoDB")


def is_over_one_month(date1, date2):
    # Calculate the difference using relativedelta
    difference = relativedelta(date2, date1)

    # Check if the number of months is greater than 1
    return difference.years > 0 or difference.months > 0


# Function to be scheduled
def task_manager_job():
    print("Task manager Job ran at:", time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        # Find the tasks
        tasks = database["tasks"].find({
            "success": False,
        })
        servers = database["emulators"].distinct("server")

        for task in tasks:
            for server in servers:
                # If one emulator is live now
                emulator = database["emulators"].find_one({
                    "server": server,
                    "status": 1,
                })

                if emulator is not None:
                    continue

                # Find the enabled emulator
                emulator = database["emulators"].find_one({
                    "server": server,
                    "usable_num": {"$gt": 0},
                    "status": 0,
                })

                if emulator is None:
                    emulator = database["emulators"].find_one({
                        "server": server,
                        "usable_num": {"$gt": 0},
                        "status": 2
                    })

                    if emulator is None:
                        continue

                    # Turn on the emulator
                    url = f"http://{emulator['server']}:5000/command"

                    r = requests.post(url, json={
                        "command": f"launch --name \"{emulator["name"]}\"",
                    })
                    if r.status_code == 200:
                        print(r.json())

                    database["emulators"].update_one({
                        "id": emulator["id"]
                    }, {
                        "$set": {
                            "status": 0,
                        }
                    })
                else:
                    award(database, emulator, task)
                break
    except Exception as e:
        print(f"An error occurred: {e}")


def instance_manager_job():
    print("Instance manager Job ran at:", time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        # Find the emulators
        emulators = database["emulators"].find({
            "status": 0,
            "usable_num": 0,
        })

        # Check the emulator
        for emulator in emulators:

            today = datetime.today()
            em_date = datetime.strptime(emulator["date"], "%Y-%m-%dT%H:%M:%S.%f")
            if is_over_one_month(em_date, today):
                database["emulators"].update_one({
                    "id": emulator["id"],
                }, {"$set": {
                    "usable_num": 2,
                    "status": 0,
                    "date": datetime.today
                }})
            else:
                url = f"http://{emulator['server']}:5000/command"
                r = requests.post(url, json={
                    "command": f"quit --name \"{emulator["name"]}\"",
                })
                if r.status_code == 200:
                    print(r.json())
                database["emulators"].update_one({
                    "id": emulator["id"]
                }, {
                    "$set": {
                        "status": 2,
                    }
                })

    except Exception as e:
        print(f"An error occurred: {e}")


# Schedule the job every minute
schedule.every(5).seconds.do(task_manager_job)
# schedule.every(5).seconds.do(instance_manager_job)

while True:
    schedule.run_pending()  # Run pending tasks
    time.sleep(1)  # Sleep for a second to avoid high CPU usage
