import sqlite3

class CalculosModel:
    def __init__(self, calculos_db="calculos.db"):
        self.calculos_db = calculos_db
        self.calculos_table()

    def calculos_table(self):
        with sqlite3.connect(self.calculos_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS calculos
                           (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           numero INTEGER NOT NULL,
                           dobro INTEGER NOT NULL,
                           triplo INTEGER NOT NULL,
                           rq REAL NOT NULL
                           )
                           """)
            conn.commit()

    def calculos_insert(self, numero, dobro, triplo, rq):
        with sqlite3.connect(self.calculos_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO calculos(numero, dobro, triplo, rq) VALUES(?, ?, ?, ?)", (numero, dobro, triplo, rq))
            conn.commit()

    def calculos_list(self):
        with sqlite3.connect(self.calculos_db) as conn:
            cursor = conn.cursor()
            response = cursor.execute("SELECT * FROM calculos ORDER BY id DESC LIMIT 1").fetchall()
            return response