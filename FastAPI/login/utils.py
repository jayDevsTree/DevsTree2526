from passlib.context import CryptContext
password_context = CryptContext(schemes = ["bcrypt"], deprecated= "auto")

def hash(password:str):
    password_encrypt = password_context.hash(password)
    return password_encrypt
