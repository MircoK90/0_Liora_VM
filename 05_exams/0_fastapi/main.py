# main.py

from fastapi import FastAPI, HTTPException, Depends
from data import load_questions
from auth import get_current_user
from logic import generate_mcq

api = FastAPI()

# load questions into a df
path = "questions_en.xlsx"
QUESTIONS = load_questions(path)

@api.get("/")
def get_index():
    return {"Starup" : "landing_page"}


@api.get("/health")
def health():
    return {"status": "ok"}
# expl see *


@api.get("/questions")
def get_questions(user: str = Depends(get_current_user)):
    return QUESTIONS


@api.get("/mcq")
# main functionality
def get_mcq(
    use:str,
    subjects:str,
    n: int = 5,
    username: str=Depends(get_current_user)
):
    try:
        result = generate_mcq(QUESTIONS, use, subjects.split(","), n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return result




# *
# Depends runs get_current_user before executing this endpoint.
# If auth fails, get_current_user raises a 401 and the request stops there.

# in principe this one:
# def get_questions(authorization: str = Header(None)):
#     username, password = parse_basic_auth(authorization)
#     user = get_current_user(username, password)
#     return QUESTIONS
