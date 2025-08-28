from fastapi import FastAPI,Depends,HTTPException,status
from typing import Optional,List
from sqlalchemy.orm import Session
import models
# from . import models
import schema,utils
# from login import models,schema
from database import engine,get_db
# from .database import get_db,engine
# from login.database import engine


models.Base.metadata.create_all(bind=engine)

app= FastAPI()

@app.get("/")
def login_root():
    return {"Message": "This represents Login Page"}

@app.post("/createUser",status_code = status.HTTP_201_CREATED,response_model = schema.userOut)
def create_user(user:schema.userCreate,db : Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    

