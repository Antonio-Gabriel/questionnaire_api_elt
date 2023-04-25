from ..answers_interface import AnswersInterface
from ...database.database_connetor import DatabaseConnector


class AnswersImplementation(AnswersInterface):
    def save_bulk(self, answers: dict):
        """save bulk answers data"""

        query = """
            INSERT INTO answers(id, question_id, text, is_correct) VALUES (?, ?, ?, ?)         
        """

        conn = DatabaseConnector.get_connection()
        conn.execute(query, list(answers.values()))
        conn.commit()
        conn.close()
