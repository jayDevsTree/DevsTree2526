import models, schema,utils
from fastapi import FastAPI,Depends,HTTPException,status,APIRouter    
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get("/getUser/{id}",response_model = schema.userOut)
def get_user(id:int,db:Session = Depends(get_db)):
    get_user = db.query(models.Users).filter(models.Users.id ==id).first()
    
    if get_user == None:
        raise HTTPException(status_code = 404, detail = f"User with id:{id} Not Found")
    
    return get_user

@router.post("/createUser",status_code = status.HTTP_201_CREATED,response_model = schema.userOut)
def create_user(user:schema.userCreate,db : Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    


