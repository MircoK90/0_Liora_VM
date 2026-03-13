# logic.py
import random
from models import Question

# Requriement
VALID_COUNTS = {5, 10, 20}


def filter_questions(questions: list[Question], use: str, subjects: list[str]) -> list[Question]:
    """filters (use) ans categories (subjects)."""
    return [
        q for q in questions
        if q.use == use and q.subject in subjects
    ]


def select_random(questions: list[Question], n: int) -> list[Question]:
    """Select random questions."""
    if n not in VALID_COUNTS:
        raise ValueError(f"Unvalid Number of selected questions: {n}. Allowed are {VALID_COUNTS}.")

    if len(questions) < n:
        raise ValueError(f"Not enough questions available: {len(questions)} < {n}")

    return random.sample(questions, n)


def generate_mcq(questions: list[Question], use: str, subjects: list[str], n: int) -> list[Question]:
    """Returns the final question compilation. Combines filter + random from file logic"""
    filtered = filter_questions(questions, use, subjects)
    selected = select_random(filtered, n)
    return selected

