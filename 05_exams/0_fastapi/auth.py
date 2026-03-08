# auth.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi import Header


USERS = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin" : "4dm1N"
}
ADMIN_PW = "4dm1N"



# section validation not encrypted

def parse_basic_auth(authorization: str = Header(...)):             # gets its in good forma from fastapi with func name
    raw =[]
    if not authorization.startswith("Basic "):
        raise HTTPException(status_code=401, detail="Invalid authentication Format")

    raw = authorization[6:] # why 6, ah due Basic_
    if ":" not in raw:
        raise HTTPException(status_code=401, detail="Invalid authentication Format")

    username, password = raw.split(":", 1) # 1 due after :?
    return  username, password


# 
def get_current_user(auth: str = Depends(parse_basic_auth)):
    username, password = auth
    if username not in USERS or USERS[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if username in USERS and USERS[username] == password:
        return username
        

def require_admin(auth = Depends(parse_basic_auth)):
    username, password = auth

    if username in USERS and USERS[username] == ADMIN_PW:           # whoever the pw have, he would have access. lets see if Line 
        return username, password
    
    if password != ADMIN_PW:
        raise HTTPException(status_code=403, detail="Admin privileges required")

    return username

# print("test_auth_runtrough")

