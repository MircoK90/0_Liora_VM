# main.py

from fastapi import FastAPI, HTTPException, Depends
from data import load_questions
from models import Question, NewQuestion
from auth import parse_basic_auth
from logic import generate_mcq
from auth import USERS, ADMIN_PW, get_current_user

api = FastAPI()

@api.on_event("startup")               # put all qestions into ram or so
def startup_event():
    global QUESTIONS
    QUESTIONS = load_questions("questions_en.xlsx")

@api.get("/health")
def health():
    return {"status": "ok"}



@api.get("/questions")
def get_questions(user: str = Depends(get_current_user)):
    return QUESTIONS







# Seection MK 
# start command
# uvicorn main:api --reload --host 0.0.0.0 --port 8000