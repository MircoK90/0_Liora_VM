# main.py

from fastapi import FastAPI, HTTPException, Depends
from data import load_questions
from models import Question, NewQuestion
from auth import parse_basic_auth
from logic import generate_mcq
from auth import USERS, ADMIN_PW, get_current_user
from fastapi.responses import FileResponse

api = FastAPI()

# pre 
path = "questions_en.xlsx"
QUESTIONS = load_questions(path)     # forgott()!

@api.get("/")
def get_index():
    return {"Starup" : "landing_page"}



@api.get("/health")
def health():
    return {"status": "ok"}



@api.get("/questions")

def get_questions(user: str = Depends(get_current_user)):
    return QUESTIONS


@api.get("/mcq")
def get_mcq(
    use:str,
    subjects:str,
    n: int = 5,
    username: str=Depends(get_current_user)
):
    try:
        result = generate_mcq(QUESTIONS, use, subjects.split(","), n)       #split is important to iterate via the 
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return result
    # testing localhost:8000/mcq?use=Validation test&subjects=Distributed systems&n=5
    #  curl -H "Authorization: Basic alice:wonderland" \
    # "http://localhost:8000/mcq?use=Positioning%20test&subjects=Databases&n=5"
    #  curl -H "Authorization: Basic alice:wonderland "http://localhost:8000/mcq?use=Positioning%20test&subjects=Databases&n=5"

    # curl -H Authorization: Basic <>

@api.get("/quiz")
def get_quiz():
    return FileResponse("quiz.html")



# Seection MK 
# start command
# uvicorn main:api --reload --host 0.0.0.0 --port 8000
# uvicorn main:api --host 0.0.0.0 --port 8000
# localhost:8000
# git push