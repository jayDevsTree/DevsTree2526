from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

my_posts= [{"title":"book","content":"this is a Book sample","id":1},
           {"title":"Movie", "content":"Avatar the last air bender", "id": 2}]

class post(BaseModel):
    title : str
    content: str
    isright : bool = False
    star : Optional[int] = None
    


@app.get("/")
async def root():
    return {"Message":"This is a Root Message from Array file"}

@app.post("/createPost")
def samplePost(post : post):
    print(post.title)
    print(post.content)
    print(post.dict())
    return{"data":"This is a Post Request"}

@app.get("/arraySee")
def array_get():
    return {"data": my_posts}
    
    