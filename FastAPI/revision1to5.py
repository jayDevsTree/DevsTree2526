from fastapi import FastAPI,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return{"Message":"This is a sample class just check revision of 1 to 5 lectures"}

class postBase(BaseModel):
    id : int
    name:str
    title: str
    content: Optional[str] = None
    
hardcode_data= [{"id":1,"name":"jay","title":"FastAPI","content":"Writing FastAPI"},
                {"id":2,"name":"Devarsh","title":"PostgreSQL"}]


@app.post("/posts")# this can normal create post which append hardcode data
def get_posts():
    return {"data":hardcode_data}
    
@app.post("/posts/body") # this is post that fetch Body of post using fastapi.params in Body 
def get_posts_body(Body_post:dict = Body(...)):
    return {"data":Body_post}

@app.post("/posts/baseModel") # this is post that fetch Body of post using pydantic
def get_posts_class(post: postBase):
    return {"data":post}

def find_dynamic_post_id(id):
    
    for post in hardcode_data:
        if post["id"] == id:
            return post

@app.get("/posts/{id}",status_code=status.HTTP_201_CREATED)# im change 200 to 201 for fetched dynamic id post

def get_posts_dynamic_id(id:int): # this is post that fetch dymnamic id url and also handle exception
    print(type(id))
    dynamic_id_post = find_dynamic_post_id(id)
    if not dynamic_id_post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"post with id:{id} not found")
    return {"data":dynamic_id_post}