import sqlite3

class DataBase:
    def __init__(self, people="people.db"):
        self.people = people
        self.people_table()


    def drop_table(self):
        with sqlite3.connect(self.people) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE people")
            conn.commit()
        
    def people_table(self):
        with sqlite3.connect(self.people) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS people
                           (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           person TEXT NOT NULL
                           )
            """)
            conn.commit()

    def people_insert(self, people):
         with sqlite3.connect(self.people) as conn:
              cursor = conn.cursor()
              cursor.execute("INSERT INTO people(person) VALUES(?)", (people,))
              cursor = conn.cursor()
              
              
              conn.commit()

    def response_model(self):
        with sqlite3.connect(self.people) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM people ORDER BY id DESC LIMIT 1")
            
            return cursor.fetchall()