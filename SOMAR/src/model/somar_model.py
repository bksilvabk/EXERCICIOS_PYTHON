import sqlite3

class SomarModel:
    def __init__(self, somar_db="somar.db"):
        self.somar_db = somar_db
        self.somar_table()

    def somar_table(self):
        with sqlite3.connect(self.somar_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS soma
                           (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           valor INTEGER
                           )
                           """)
            conn.commit()

    def somar_insert(self, valor_user):
        with sqlite3.connect(self.somar_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO soma(valor) VALUES(?)", (valor_user,))
            conn.commit()

    def somar_list(self):
        with sqlite3.connect(self.somar_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM (SELECT valor FROM soma ORDER BY id DESC LIMIT 2) ORDER BY valor ASC")
            return cursor.fetchall()