# data.py  "read from df"

import pandas as pd
from models import Question
from logic import generate_mcq


def load_questions(path: str) -> list[Question]:
	df = pd.read_excel(path).fillna("").astype(str)
	questions = []
	for _ , row in  df.iterrows():
		q = Question(
		question=row["question"],
		subject=row["subject"],
		use=row["use"],
		correct=row["correct"],
		answerA=row["responseA"],
		answerB=row["responseB"],
		answerC=row.get("responseC"),
		answerD=row.get("responseD"),
		)
		questions.append(q)
	return questions



if __name__ == "__main__":
    print(f"Q: {q.question}")
    print(f"A: {q.answerA}")
    print(f"B: {q.answerB}")
    if q.answerC:
        print(f"C: {q.answerC}")
    if q.answerD:
        print(f"D: {q.answerD}")
    print(f"Correct: {q.correct}")
    print("-" * 40)
    print("finished loading questions")








