import sqlite3


class TarefasModel:

    def __init__(self, database = "gerenciador_tarefas.db"):
        self.database = database
        self.tarefas_table()

    def drop_table(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE tarefas")
            conn.commit()

    def tarefas_table(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas
                           (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           tarefa TEXT NOT NULL,
                           status INTEGER NOT NULL DEFAULT 0
                           )
                           """)
            conn.commit()


    def tarefas_insert(self, tarefa):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tarefas(tarefa) VALUES(?)", (tarefa,))
            conn.commit()


    def tarefas_read(self):
        with sqlite3.connect(self.database) as conn:
            cursor =conn.cursor()
            cursor.execute("SELECT * FROM tarefas")
            conn.commit()
            return cursor.fetchall()


    def tarefas_update(self, tarefa, id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE tarefas SET 
                           tarefa = ?
                           WHERE id = ?
                           """, (tarefa, id))
            conn.commit()
    
    
    def tarefas_update_status(self, status, id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tarefas SET status = ? WHERE id = (?)", (status, id))
            conn.commit()


    def tarefas_delete(self, id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tarefas WHERE id = (?)", (id,))
            conn.commit()


    def get_by_id(self, id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tarefas WHERE id = (?)", (id,))
            conn.commit()
            return cursor.fetchone()


    def tarefas_delete_all(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tarefas")
            conn.commit()