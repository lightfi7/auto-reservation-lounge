from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from pymongo import MongoClient
from src.routes.api import router as api_router
load_dotenv()

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongo_client = MongoClient('mongodb://localhost:27017/')
    app.db = app.mongo_client['lounge']
    print("Connected to MongoDB")
    yield
    # Clean up the ML models and release the resources
    app.mongo_client.close()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)