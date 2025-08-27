from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
import models
from database import engine,get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



class post(BaseModel):
    title: str
    content: Optional[str]
    
    
@app.get("/")
async def root():
    return{"Message": "This is a root path of Sqlalchemy Setup"}

@app.get("/sqlalchemy")
def sqlalchemy_test(db: Session = Depends(get_db)):
    return {"Message": "This is a Sqlalchemy Setup"}

@app.get("/getAllPost")
def getAllPost(db: Session = Depends(get_db)):
    posts= db.query(models.Post).all()
    return {"data": posts}

@app.post("/createPost")
def createPost(post:post, db: Session = Depends(get_db)):
    # new_post =models.Post(title = post.title, content = post.content)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}

@app.delete("/deletePost/{id}")
def deletePost(id:int,db: Session = Depends(get_db)):
    get_delete_post = db.query(models.Post).filter(models.Post.id == id)
    if get_delete_post.first() == None:
        raise HTTPException(status_code = 404,
                           detail = f"Post with id:{id} Not Found")
    # get_delete_post.delete(synchronize_session=False)
    get_delete_post.delete()
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)
    
@app.put("/updatePost/{id}")
def updatePost(id:int,post:post,db: Session = Depends(get_db)):
    get_update_post = db.query(models.Post).filter(models.Post.id == id)
    if get_update_post.first()==None:
        raise HTTPException(status_code = 404,
                           detail = f"Post with id:{id} Not Found")
    # get_update_post = get_update_post.update(post.dict(),synchronize_session=False)   
    get_update_post = get_update_post.update(post.dict())  
    db.commit()
    return {"data": get_update_post}

@app.post("/getPosts/{id}")
def get_post(id:int,post:post,db: Session = Depends(get_db)):
    get_post = db.query(models.Post).filter(models.Post.id == id).first()
    if get_post == None:
        raise HTTPException(status_code = 404,
                           detail = f"Post with id:{id} Not Found")
    return {"post Detail": get_post}
    