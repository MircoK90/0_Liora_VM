# logic.py
import random
from models import Question

VALID_COUNTS = {5, 10, 20}   # from the task

def filter_questions(questions: list[Question], use: str, subjects: list[str]) -> list[Question]:
    """filters (use) ans categories (subjects)."""
    return [
        q for q in questions
        if q.use == use and q.subject in subjects
    ]


def select_random(questions: list[Question], n: int) -> list[Question]:
    """Select random questions."""
    if n not in VALID_COUNTS:
        raise ValueError(f"Ungültige Anzahl: {n}. Erlaubt sind {VALID_COUNTS}.")

    if len(questions) < n:
        raise ValueError(f"Nicht genug Fragen vorhanden: {len(questions)} < {n}")

    return random.sample(questions, n)


def generate_mcq(questions: list[Question], use: str, subjects: list[str], n: int) -> list[Question]:
    """Kombiniert Filter + Zufallsauswahl."""
    filtered = filter_questions(questions, use, subjects)
    selected = select_random(filtered, n)
    return selected

