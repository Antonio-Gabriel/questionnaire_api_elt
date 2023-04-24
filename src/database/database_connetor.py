import sqlite3, os

class DatabaseConnector:
    @staticmethod
    def get_connection():
        """database connection instance"""
        con = sqlite3.connect(os.environ["URL_BASE"])
        return con
