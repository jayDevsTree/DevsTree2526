from sqlalchemy import Column,Integer,String,Boolean
# from .database import Base
from database  import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP



class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key = True,nullable = False)
    email = Column(String,nullable= False,unique = True)
    password = Column(String,nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default = text('now()'))
    
