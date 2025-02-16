import sqlite3

class DataBase:
    DATABASE = "gestao_estoque.db"

    @staticmethod
    def connect():
        return sqlite3.connect(DataBase.DATABASE)