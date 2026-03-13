# data.py  "read from df"

import pandas as pd
from models import Question
from logic import generate_mcq

# Formats and saves the question in a class 
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


# _______________________________________
# testing MK
# _______________________________________


# if __name__ == "__main__":							# cleaner method to test the loading of questions, only runs when this file is executed directly, not when imported
# 	questions = load_questions("questions_en.xlsx")

# 	for q in questions:
# 		print(f"Q: {q.question}")
# 		print(f"A: {q.answerA}")
# 		print(f"B: {q.answerB}")
# 		if q.answerC:
# 			print(f"C: {q.answerC}")
# 		if q.answerD:
# 			print(f"D: {q.answerD}")
# 		print(f"Correct: {q.correct}")
# 		print("-" * 40)

# print("finished loading questions")

# questions = load_questions("questions_en.xlsx")
# generated = generate_mcq(questions = questions, use="Positioning test", subjects=["Distributed systems"], n=5)

# for q in generated:
# 	print(f"Q: {q.question}")
# 	print(f"A: {q.answerA}")
# 	print(f"B: {q.answerB}")
# 	if q.answerC:
# 		print(f"C: {q.answerC}")
# 	if q.answerD:
# 		print(f"D: {q.answerD}")
# 	print(f"Correct: {q.correct}")
# 	print("-" * 40)



# print("updated on github")
