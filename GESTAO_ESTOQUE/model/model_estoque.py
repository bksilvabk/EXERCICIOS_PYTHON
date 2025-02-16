from model.database import DataBase

class EstoqueModel:
    def __init__(self):
        self.estoque_table()


    def drop_table(self):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE estoque")
            conn.commit()
        


    def estoque_table(self):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS estoque(
                           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                           produto TEXT NOT NULL,
                           quantidade INTEGER NOT NULL,
                           preco REAL NOT NULL,
                           total REAL NOT NULL,
                           status INTEGER NOT NULL DEFAULT 0
                           );""")
            conn.commit()


    def estoque_insert(self, produto, quantidade, preco, total):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO estoque(produto, quantidade, preco, total) VALUES(?, ?, ?, ?)", (produto, quantidade, preco, total))
            conn.commit()


    def estoque_read(self, limite, offset):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estoque LIMIT ? OFFSET ?", (limite, offset))
            conn.commit()
            return cursor.fetchall()





    def estoque_update(self, produto, quantidade, preco, total, id):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE estoque SET produto = ?, quantidade = ?, preco = ?, total = ? WHERE id = ?", (produto, quantidade, preco, total, id))


    def estoque_delete(self, id):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estoque WHERE id = ?", (id,))


    def estoque_delete_all(self):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estoque")
            conn.commit()

    
    def estoque_get_by_id(self, id):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estoque WHERE id = ?", (id,))
            conn.commit()
            return cursor.fetchone()


    def buscar(self, produto, preco):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estoque WHERE produto LIKE ? AND preco LIKE ?", (f"%{produto}%", f"%{preco}%"))
            conn.commit()
            return cursor.fetchall()