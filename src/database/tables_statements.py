from .database_connetor import DatabaseConnector

class TableStatements:
    @staticmethod
    def create_table():
        """create tables"""

        questions_query = '''
            CREATE TABLE IF NOT EXISTS questions(
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP                
            );            
        '''

        answers_query = '''
            CREATE TABLE IF NOT EXISTS answers(
                id TEXT PRIMARY KEY,
                text TEXT NOT NULL,
                question_id TEXT NOT NULL,
                is_correct NUMERIC NOT NULL,
                date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (question_id)
                        REFERENCES questions(id)
                        ON DELETE SET NULL               
            )         
        
        '''
        
        conn = DatabaseConnector.get_connection()
        cursor = conn.cursor()
        cursor.execute(questions_query)
        cursor.execute(answers_query)
        cursor.close()
        conn.commit()
