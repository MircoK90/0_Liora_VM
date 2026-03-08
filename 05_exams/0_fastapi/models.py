# models.py

from pydantic import BaseModel, Field
from typing import Optional, List

class Question(BaseModel):       # BaseModel converts API Format trough Json() conversion
	question: str
	subject: str
	use: str
	correct: str
	answerA: str
	answerB: str
	answerC: Optional[str]=None
	answerD: Optional[str]=None  	  #mk col remark is ignored



	def answers(self) ->List[str]:
		"""Gives back all exsiting answers"""
		out = [self.answerA, self.answerB]
		if self.answerC:
			out.append(self.answerC)
		if self.answerD:
			out.append(self.answerD)
		return out           #remark is ignored


class NewQuestion(BaseModel):
	question: str
	subject: str
	use: str
	correct: str = Field(..., min_length=1, max_length=1)		# check here is the only difference to Question
	answerA: str
	answerB: str
	answerC: Optional[str] = None
	answerD: Optional[str] = None

print("test_yeah") # dows it tun with nano and in the VM
