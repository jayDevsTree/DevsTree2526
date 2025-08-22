from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "This is First time try FastAPI"}

@app.get("/posts")
def posts():
    return {"message": "this is a Post Page"}

@app.post('/createPost')
def create_Post():
    return {"message": "Post Created"}