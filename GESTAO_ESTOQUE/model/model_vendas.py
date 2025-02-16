from model.database import DataBase

class VendasModel:
    def __init__(self):
        self.vendas_table()


    def drop_table(self):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE vendas")


    def vendas_table(self):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS vendas(
                           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                           produto TEXT NOT NULL,
                           quantidade INTEGER NOT NULL,
                           valor_venda REAL NOT NULL,
                           datahora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                           estoque_id INTEGER NOT NULL,
                           FOREIGN KEY(estoque_id) REFERENCES estoque(id)
                           );""")
            conn.commit()


    def vendas_insert(self, estoque_id, produto, quantidade, valor_venda, data_hora):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vendas(estoque_id, produto, quantidade, valor_venda, datahora) VALUES(?, ?, ?, ?, ?)", (estoque_id, produto, quantidade, valor_venda, data_hora))
            conn.commit()


    def vendas_read(self):
        with DataBase.connect() as  conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas")
            conn.commit()
            return cursor.fetchall()


    def vendas_success(self):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas ORDER BY id DESC LIMIT 1")
            conn.commit()
            return cursor.fetchone()


    def update_estoque_by_vendas(self, calc_quant, total, id):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE estoque SET quantidade = ?, total = ? WHERE id = ?""", (calc_quant, total, id))


    def relatorio_geral(self):
        with DataBase.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT SUM((e.preco * 2.1) * v.quantidade)  AS receita_vendas,
                           SUM(e.preco * v.quantidade) AS custo_produto,
                           SUM(((e.preco * 2.1) * v.quantidade) - (e.preco * v.quantidade)) AS lucro_liquido
                           FROM vendas v JOIN estoque e ON v.estoque_id = e.id""")
            conn.commit()
            return cursor.fetchall()