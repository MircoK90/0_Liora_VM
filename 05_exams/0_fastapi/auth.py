# auth.py

from fastapi import FastAPI, HTTPException, Depends

USERS = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine"
}

ADMIN_PW = "MIRCO"


def parse_basic_auth(auth_header: str):             # gets its in good forma from fastapi with func name
    raw =[]
    if not auth_header.startswith("Basic "):
        raise HTTPException(status_code=401, detail="Invalid authentication Format")

    raw = auth_header[6:] # why 6

    if ":" not in raw:
        raise HTTPException(status_code=401, detail="Invalid authentication Format")
    username, password = raw.split(":")

    return  username, password






#_____________ Testing
# print("RAW:", auth_header)