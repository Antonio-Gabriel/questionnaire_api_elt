from uuid import uuid4


from ...errors.transform_error import TransformError
from ..contracts.extract_contract import ExtractContract
from ..contracts.transform_contract import TransformContract


class TransformRawData:
    def __init__(self) -> None:
        self.answers = []
        self.questions = []

    def transform(self, extract_contract: ExtractContract) -> TransformContract:
        """Transform questionnaire extracted data"""      
        self.__reset_lists()
        
        try:
            raw_data = extract_contract.raw_information_content

            for data in raw_data:               
                question = data.get('question')
                answers_data = data.get('answers')
             
                if question:
                    question_id = str(uuid4())
                    question_item = {
                        "id": question_id,
                        "title": question                        
                    }
                                       
                    self.questions.append(question_item)                            

                    # Validate answers and correctors
                    for answer_key, answer_value in answers_data.items():
                        if answer_value is not None:                                                    
                            is_correct = self.__validate_corrector(data['correct_answers'][f"{answer_key}_correct"])
                            answer_item = self.__answers_payload(question_id, answer_value, is_correct)
                            
                            if not self.__check_limit_of_answers(question_id):                        
                                self.answers.append(answer_item)                            
                                                                    
            return TransformContract(
                questions=self.questions,            
                answers=self.answers
            )
        except Exception as exception:
            raise TransformError(str(exception.args)) from exception

    @staticmethod
    def __validate_corrector(correct_answer: str) -> bool:
        """Check if the answer is correct"""
        return correct_answer.lower() == "true"

    @staticmethod
    def __answers_payload(question_id: str, text: str, is_correct: bool) -> dict:
        """Answer payload"""
        return {
            "id": str(uuid4()),
            "question_id": question_id,
            "text": text,
            "is_correct": is_correct
        }

    def __check_limit_of_answers(self, key: str):
        """check the limits of answers per question"""

        answers = [q for q in self.answers if q['question_id'] == key]
        answers_count = len(answers)

        if answers_count != 4:
            return False

        return True
        
    def __reset_lists(self) -> None:
        """Reset the instance lists"""
        self.answers = []
        self.questions = []
