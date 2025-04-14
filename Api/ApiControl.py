from Api.IApi import IApi
from fastapi import FastAPI
from Api.routers import router as task_router
import uvicorn



class FastApiControl(IApi):
    def __init__(self, db):
        self.db = db


    def run(self):
        app = FastAPI(title="ToDo App")
        app.include_router(task_router)
        uvicorn.run(app, host="0.0.0.0", port=8000)
