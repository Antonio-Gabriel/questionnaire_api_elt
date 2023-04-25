from abc import ABC, abstractmethod

class QuestionsInterface(ABC):
    
    @abstractmethod
    def save_bulk(self, questions: dict):
        """save bulk question from database"""

        raise NotImplementedError("Method not implemented")
    
    @abstractmethod
    def get_questions(self):
        """get all questions from db"""

        raise NotImplementedError("Method not implemented")
