from abc import ABC, abstractmethod

class AnswersInterface(ABC):
    
    @abstractmethod
    def save_bulk(self, answers: dict):
        """save bulk abswers from database"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_answers(self):
        """get all answers from db"""

        raise NotImplementedError("Method not implemented")
