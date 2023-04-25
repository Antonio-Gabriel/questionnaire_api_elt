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

    def get_answers(self):
        """get all answers from db"""

        query = ''' SELECT * FROM answers '''

        conn = DatabaseConnector.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        answers = cursor.fetchall()
        cursor.close()
        conn.close()

        return answers
