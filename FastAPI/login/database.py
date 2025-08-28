from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

def database_url():
    load_dotenv("../db.env")
    user = os.getenv("DB_USER")
    password= os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")
    
    SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"
    
    return SQLALCHEMY_DATABASE_URL

engine = create_engine(database_url())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

