from ..models.answer_model import AnswerModel, AnswerMapper

def answer_mapper(answers: list):
    """answers mapper response"""
    answers_mapped = []

    for question in answers:
        answer_model = AnswerModel(
            id=question[0], question_id=question[2], text=question[1],
            is_correct=question[3], created_at=question[4])
        
        answer_bind = AnswerMapper.build_from_model(answer_model)

        answers_mapped.append(answer_bind.dict())
        
    return answers_mapped
