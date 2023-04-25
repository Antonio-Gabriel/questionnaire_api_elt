from typing import List
from fastapi import FastAPI, status

from .mappers.answer_mapper import answer_mapper, AnswerModel
from .mappers.question_mapper import question_mapper, QuestionModel
from ..services.implementation.questions_implementation import (
    QuestionsImplementation
)

from ..services.implementation.answers_implementation import (
    AnswersImplementation
)

app = FastAPI()

@app.get("/questions", 
         status_code=status.HTTP_200_OK)
def get_questions() -> List[QuestionModel]:
    """get all questions from database"""

    question_impl = QuestionsImplementation()
    questions = question_mapper(question_impl.get_questions())

    return questions


@app.get("/answers",
         status_code=status.HTTP_200_OK
         )
def get_answers() -> List[AnswerModel]:
    """get all answers from database"""

    answer_impl = AnswersImplementation()
    answers = answer_mapper(answer_impl.get_answers())

    return answers
