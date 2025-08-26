from fastapi import FastAPI,status,Response,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

data = [{"id":1,"name":"jay","title":"FastAPI","content":"Writing FastAPI"},
    {"id":2,"name":"Devarsh","title":"PostgreSQL"},
    {"id":3,"name":"Talha","title":"Django"}]

class postBase(BaseModel):
    id:int
    title:str
    content:Optional[str]
    published:bool
    created_at:datetime = Field(default_factory=datetime.now)


@app.get("/")
def root():
    return {"Message": "This Code Perform CRUD in FastAPI"}

@app.get("/getAllPost")
def allPost():
    return {"data": data}

@app.post("/createPost")
def createPost(post:postBase):
    post_dict = post.dict()
    post_dict["id"] = randrange(1,10000)
    data.append(post_dict)
    return {"data": data}

def get_dynamic_id(id):# this return object(dictionary) of that id in data
    for post in data:
        if post["id"] == id:
            return post
    return None

def get_index(id):# this return index (starts from 0,1,2...) a number not whole object(dictonary)
    for index,post in enumerate(data):
        if post["id"]== id:
            return index
    return None

@app.get("/getPost/{id}",status_code=status.HTTP_200_OK)
def getPost(id:int):
    get_post = get_dynamic_id(id)
    if get_post == None:
        raise HTTPException(status_code = 404,
                            detail = f"Post with id:{id} Not Found")
    return{"data":get_post}    

@app.put("/updatePost/{id}")
def updatePost(id:int,post:postBase):
    index= get_index(id)
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id:{id} does not Exists")
        
    data[index] = post.dict()
    return {"data": data}

@app.delete("/deletePost/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deletePost(id:int):
    
    delete_index = get_index(id)
    if delete_index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id:{id} does not Exists")
    data.pop(delete_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

    # delete_index = get_dynamic_id(id)
    # if delete_index == None:
    #     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
    #                         detail = f"Post with id:{id} does not Exists")
    # data.remove(delete_index)
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
    


    

