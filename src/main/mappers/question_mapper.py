from ..models.question_model import QuestionModel, QuestionMapper

def question_mapper(questions: list):
    """articles responses"""
    questions_mapped = []

    for question in questions:
        question_model = QuestionModel(
            id=question[0], title=question[1], created_at=question[2])
        
        question_bind = QuestionMapper.build_from_model(question_model)

        questions_mapped.append(question_bind.dict())
        
    return questions_mapped
