from time import sleep

class EstoqueView:
    def estoque_response(self, response):
        print(f"\n$\n{response}\n$")


    def menu_view_principal(self):
        while True:
            try:
                op = int(input("""
=============================
== GESTÃO DE ESTOQUE       ==
=============================
== [1] ADICIONAR - PRODUTO ==
== [2] LISTAR - PRODUTO    ==
== [3] EDITAR - PRODUTO    ==
== [4] DELETAR - PRODUTO   ==
== [5] VENDER - PRODUTO    ==
== [6] RELATÓRIO - VENDAS  ==
== [7] RELATÓRIO - GERAL   ==
== [8] PESQUISAR - PRODUTO ==
== [321] DELETAR - TUDO    ==
== [0] SAIR                ==
=============================
ESCOLHA: """))
                return op
            except ValueError:
                self.estoque_response("ERRO: OPÇÃO INVALIDA, TENTE NOVAMENTE!")



    def estoque_view_get_id(self):
        id = int(input("ID do produto: "))
        return id
    

    def buscar(self):

        nome = str(input("Buscar produto por nome: ")).strip().capitalize()
        preco = float(input("Buscar produto por preço: "))
        return nome, preco
    

    def estoque_view_input(self):
        produto = str(input("\nProduto: ")).strip().capitalize()
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        total = quantidade * preco
        return produto, quantidade, preco, total


    def estoque_view_list(self, list_, status):
            print(f"""
ID: {list_[0]}
PRODUTO: {list_[1]}
QUANTIDADE: {list_[2]}
PREÇO: R${list_[3]:.2f}
TOTAL: R${list_[4]}
STATUS: {status}
""")
    

    def vendas_view_input(self):
        id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade para vendas: "))
        return id, quantidade


    def relatorio_vendas(self, list_):
            print(f"""
BASE DE CALCULO PARA VENDA: preço x 2.1 = 110% de lucro...

VENDAS_ID: {list_[0]}
PRODUTO: {list_[1]}
QUANTIDADE VENDIDO: {list_[2]}
VALOR DA VENDA: R${list_[3]:.2f}
DATA/ HORA: {list_[4]}
ESTOQUE_ID: {list_[5]}
""")
            

    def relatorio_geral(self, list_, data):
            print(f"""                  
TOTAL DE VENDAS: R${list_[0][0]:.2f}

CUSTOS TOTAL: R${list_[0][1]:.2f}

LUCRO LIQUÍDO: R${list_[0][2]:.2f}

DATA DE EMISSÃO: {data}
""")
