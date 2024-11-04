from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles
from src.routes.api import router as api_router
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongo_client = MongoClient('mongodb://127.0.0.1:27017/')
    app.database = app.mongo_client['lounge']
    print("Connected to MongoDB")
    yield
    # Clean up the ML models and release the resources
    app.mongo_client.close()

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)