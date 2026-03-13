# auth.py

from fastapi import HTTPException, Depends
from fastapi import Header


USERS = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin" : "4dm1N"
}
ADMIN_PW = "4dm1N"


def parse_basic_auth(authorization: str | None = Header(default=None)):
    """
    
    """
    if authorization is None:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if not authorization.startswith("Basic "):
        raise HTTPException(status_code=401, detail="Invalid authentication format")

    raw = authorization[6:]
    if ":" not in raw:
        raise HTTPException(status_code=401, detail="Invalid authentication format")

    username, password = raw.split(":", 1)
    return username, password



def get_current_user(auth: str = Depends(parse_basic_auth)):
    username, password = auth
    if username not in USERS or USERS[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return username


def require_admin(auth = Depends(parse_basic_auth)):
    username, password = auth

    if username != "admin" or password != ADMIN_PW:
        raise HTTPException(status_code=403, detail="Admin privileges required")

    return username

