import models, schema
from typing import Optional,List
from fastapi import FastAPI,Depends,HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine,get_db
from sqlalchemy import schema

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/getAllPost",response_model = List[schema.postOut])
def getAllPost(db: Session = Depends(get_db)):
    posts= db.query(models.Post).all()
    return posts


@router.post("/createPost",response_model = schema.postOut)
def createPost(post:schema.postBase, db: Session = Depends(get_db)):
    # new_post =models.Post(title = post.title, content = post.content)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.post("/getPosts/{id}")
def get_post(id:int,post:schema.postBase,db: Session = Depends(get_db)):
    get_post = db.query(models.Post).filter(models.Post.id == id).first()
    if get_post == None:
        raise HTTPException(status_code = 404,
                           detail = f"Post with id:{id} Not Found")
    return get_post