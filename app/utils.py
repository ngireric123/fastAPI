from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

# verify if the enter password is the same as the hashed password in database

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
