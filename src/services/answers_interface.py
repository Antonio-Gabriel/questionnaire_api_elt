from abc import ABC, abstractmethod

class AnswersInterface(ABC):
    
    @abstractmethod
    def save_bulk(self, answers: dict):
        """save bulk abswers from database"""

        raise NotImplementedError("Method not implemented")
