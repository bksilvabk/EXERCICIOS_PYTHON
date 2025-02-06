import sqlite3

class BeforAfterModel:
    def __init__(self, before_after_db = "before_after.db"):
        self.before_after_db = before_after_db
        self.before_after_table()

    def before_after_table(self):
        with sqlite3.connect(self.before_after_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS before_after
                           (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           numero INTEGER
                           )
                           """)
            conn.commit()

    def before_after_insert(self, numero):
        with sqlite3.connect(self.before_after_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO before_after(numero) VALUES(?)", (numero,))
            conn.commit()

    def before_after_list(self):
        with sqlite3.connect(self.before_after_db) as conn:
            cursor = conn.cursor()
            response = cursor.execute("SELECT numero FROM before_after ORDER BY id DESC LIMIT 1").fetchone()
            return response[0] if response else None