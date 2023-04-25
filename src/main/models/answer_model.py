from datetime import datetime
from pydantic import BaseModel, Field
from pymapme.models.mapping import MappingModel


class AnswerModel(BaseModel):
    id: str
    question_id: str
    text: str
    is_correct: bool
    created_at: datetime
    

class AnswerMapper(MappingModel):
    """mapping answer models to json"""
    id: str = Field(source='id')
    question_id: str = Field(source='question_id')
    text: str = Field(source='text')
    is_correct: bool = Field(source='is_correct')
    created_at: datetime = Field(source='created_at')
