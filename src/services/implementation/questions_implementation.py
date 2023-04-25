from ..questions_interface import QuestionsInterface
from ...database.database_connetor import DatabaseConnector


class QuestionsImplementation(QuestionsInterface):
    def save_bulk(self, questions: dict):
        """save bulk questions data"""

        query = '''
            INSERT INTO questions(id, title) VALUES (?, ?)         
        '''   

        conn = DatabaseConnector.get_connection()
        conn.execute(query, list(questions.values()))
        conn.commit()
        conn.close()
