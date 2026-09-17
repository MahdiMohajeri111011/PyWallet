import os
from dotenv import load_dotenv
from jose import jwt
from datetime import timedelta , datetime
load_dotenv()

ALGORITHEM = 'HS256'
SEKRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(user_id) :
    expire = datetime.now() + datetime(minute=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub" : str(user_id) , "exp" : expire}
    return jwt.encode(payload , SEKRET_KEY, ALGORITHEM)

def create_refresh_token(user_id) :
    expire = datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {"sub" : str(user_id) , "type" : "refresh" , "exp" : expire}
    return jwt.encode(payload, SEKRET_KEY, ALGORITHEM)






