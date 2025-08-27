from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv("../db.env")

user_name = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
host_name = os.getenv("DB_HOST")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user_name}:{password}@{host_name}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
