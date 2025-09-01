from Project1.database import engine,stock_db
from fastapi import FastAPI
from sqlalchemy.orm import Session
import users_models,users_schema

users_models.base.metadata.create_all(bind = engine)

app = FastAPI()

@app.get("/")
async def root():
    return{"Message":"This is a Users Table root Path"}