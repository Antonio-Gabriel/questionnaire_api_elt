import multiprocessing

from ...errors.load_error import LoadError
from ...services.answers_interface import AnswersInterface
from ..contracts.transform_contract import TransformContract
from ...services.questions_interface import QuestionsInterface


class LoadData:
    def __init__(self, 
                 answer_service: AnswersInterface, 
                 question_service: QuestionsInterface
                 ) -> None:
        self.__answer_service = answer_service
        self.__question_service = question_service
    
    
    def load(self, transform_extracted: TransformContract):
        """load data into local database"""

        try:
            answers = transform_extracted.answers
            questions = transform_extracted.questions

            first_process = multiprocessing.Process(target=self.__load_questions(questions))
            last_process = multiprocessing.Process(target=self.__load_answers(answers))

            # starting the first process
            first_process.start()
            first_process.join()

            last_process.start()
            last_process.join()

            print("Extraction finished")

        except Exception as exception:
            raise LoadError(str(exception)) from exception

    def __load_questions(self, questions: list):
        """save bulk questions from db"""
        for index, data in enumerate(questions):
            self.__question_service.save_bulk(data)
            
            print(f'Insertind question: {str(index + 1)}')
    
    def __load_answers(self, answers: list):
        """save bulk answers from db"""
        for index, data in enumerate(answers):            
            self.__answer_service.save_bulk(data)        
            
            print(f'Insertind answer: {str(index + 1)}')
