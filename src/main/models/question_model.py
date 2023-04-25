from datetime import datetime
from pydantic import BaseModel, Field
from pymapme.models.mapping import MappingModel


class QuestionModel(BaseModel):
    id: str
    title: str
    created_at: datetime

    # class Config:
    #     orm_mode = True

class QuestionMapper(MappingModel):
    """mapping question models to json"""
    id: str = Field(source='id')
    title: str = Field(source='title')
    created_at: datetime = Field(source='created_at')
