# main.py

from fastapi import FastAPI, HTTPException, Depends
from data import load_questions
from models import Question, NewQuestion
from auth import parse_basic_auth
from logic import generate_mcq
from auth import USERS, ADMIN_PW

api = FastAPI()

@api.on_event("startup")               # put all qestions into ram or so
def startup_event():
    global QUESTIONS
    QUESTIONS = load_questions("questions_en.xlsx")

@api.get("/health")
def health():
    return {"status": "ok"}


@api.get("/questions")
def get_questions(auth: str = Depends(parse_basic_auth)):
    username, password = auth
    if username not in USERS or USERS[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return QUESTIONS