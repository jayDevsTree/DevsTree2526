from database import get_db, engine
from typing import Optional,List
from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import models, schema, utils
from Router import user,post


models.Base.metadata.create_all(bind=engine)

app= FastAPI()

@app.get("/")
def root():
    return{"Message":"This is a router example"}

@app.get("/getUser/{id}",response_model = schema.userOut)
def get_user(id:int,db:Session = Depends(get_db)):
    get_user = db.query(models.Users).filter(models.Users.id ==id).first()
    
    if get_user == None:
        raise HTTPException(status_code = 404, detail = f"User with id:{id} Not Found")
    
    return get_user

app.include_router(user.router)
app.include_router(post.router)

