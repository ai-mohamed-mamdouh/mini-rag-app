from fastapi import FastAPI
from src.interfaces.api.routes.base import base_router
from src.interfaces.api.routes.data import data_router

app = FastAPI() 
app.include_router(base_router)
app.include_router(data_router)