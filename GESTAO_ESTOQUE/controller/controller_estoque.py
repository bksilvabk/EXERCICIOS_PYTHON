from model.model_estoque import EstoqueModel
from model.model_vendas import VendasModel
from controller.controller_vendas import ControllerVendas
from view.view import EstoqueView

class EstoqueController:
    def __init__(self):
        self.model_estoque = EstoqueModel()
        self.model_vendas = VendasModel()
        self.controller_vendas = ControllerVendas()
        self.view = EstoqueView()


    def estoque_controller_insert(self):
        try:
            produto, quantidade, preco, total = self.view.estoque_view_input()
            if produto != "":
                self.model_estoque.estoque_insert(produto, quantidade, preco, total)
                self.view.estoque_response("PRODUTO CADASTRADO COM SUCESSO!")
            else:
                self.view.estoque_response("ERRO: PREENCHA TODOS OS CAMPOS COM SEUS DEVIDOS VALORES: produto\n(texto) - quantidade(inteiro: 1,2,3 etc...) - preço(Reais: R$2.00, R$50.00 use ponto '.' \nno lugar da virgula ',')")
        except ValueError:
            self.view.estoque_response("ERRO: PREENCHA TODOS OS CAMPOS COM SEUS DEVIDOS VALORES: produto\n(texto) - quantidade(inteiro: 1,2,3 etc...) - preço(Reais: R$2.00, R$50.00 use ponto '.' \nno lugar da virgula ',')")


    def estoque_controller_list(self):
        self.view.estoque_response("$LISTA DE PRODUTOS CADASTRADOS$")
        limite = 3
        offset = 0
        while True:
            list_ = self.model_estoque.estoque_read(limite, offset)
            if not list_:
                self.view.estoque_response("NÃO HÁ MAIS PRODUTOS PARA EXIBIR!")
                break
            for lista in list_:
                quant = lista[2]                  
                status = lista[5]
                if quant > status:
                    status = "EM ESTOQUE"
                else:
                    status = "SEM ESTOQUE"
                self.view.estoque_view_list(lista, status)
            plus = str(input("\nDESEJA VER MAIS? s/n: ")).strip().lower()
            if plus == "n":
                    break
            offset += limite


    def estoque_controller_update(self):
        self.view.estoque_response("$ MENU DE EDIÇÃO DE PRODUTOS $")
        try:
            id = self.view.estoque_view_get_id()
            get = self.model_estoque.estoque_get_by_id(id)
            if get:
                self.view.estoque_response("DETALHES DO PRODUTO A SER EDITADO:")
                quant = get[2]
                status = get[5]
                if quant > status:
                    status = "EM ESTOQUE"
                else:
                    status = "SEM ESTOQUE"
                self.view.estoque_view_list(get, status)
                produto, quantidade, preco, total = self.view.estoque_view_input()
                if produto != "":
                    self.model_estoque.estoque_update(produto, quantidade, preco, total, id)
                    self.view.estoque_response("PRODUTO EDITADO COM SUCESSO!")
                else:
                        self.view.estoque_response("ERRO: OPS! CAMPO VAZIO. CORRIJA E TENTE NOVAMENTE!")
            else:
                 self.view.estoque_response("ERRO: ID INEXISTENTE, CONSULTE O MENU (LISTAR) PARA PEGAR O ID E TENTE NOVAMENTE!")
        except ValueError:
             self.view.estoque_response("ERRO: OPS! CAMPO VAZIO. CORRIJA E TENTE NOVAMENTE!")



    def estoque_controller_delete(self):
        self.view.estoque_response("$ MENU DE DELEÇÃO $")
        try:
            id = self.view.estoque_view_get_id()
            get = self.model_estoque.estoque_get_by_id(id)
            if get:
                self.view.estoque_response("DETALHES DO PRODUTO A SER DELETADO:")
                quant = get[2]
                status = get[5]
                if quant > status:
                    status = "EM ESTOQUE"
                else:
                    status = "SEM ESTOQUE"
                self.view.estoque_view_list(get, status)
                self.model_estoque.estoque_delete(id)
                self.view.estoque_response("PRODUTO DELETADO COM SUCESSO!")
            else:
                self.view.estoque_response("ERRO: ESSE ID NÃO EXISTE NO BANCO DE DADOS, VA ATÉ O (LISTAR) PARA VER OS IDs CADASTRADOS!")
        except ValueError:
            self.view.estoque_response("O CAMPO ID NÃO PODE FICAR EM BRANCO, DIGITE O ID DO PRODUTO A SER DELETADO!")


    def estoque_controller_delete_all(self):
         self.model_estoque.drop_table()
         self.model_vendas.drop_table()
         self.view.estoque_response("$ PROCESSO DE EXCLUSÃO COMPLETO $")


    def buscar(self):
        try:
            produto, preco = self.view.buscar()
            buscar = self.model_estoque.buscar(produto, preco)
            if buscar and produto != "":
                for lista in buscar:
                    status = lista[5]
                    quant = lista[2]
                    if quant > status:
                        status = "EM ESTOQUE"
                    else:
                         status = "SEM ESTOQUE"
                    self.view.estoque_view_list(lista, status)
            else:
                 self.view.estoque_response("NENHUM RESULTADO ENCONTRADO PARA ESSA BUSCA!")
        except ValueError:
             self.view.estoque_response("ERRO: TODOS OS CAMPOS DEVEM SER PREENCHIDOS PARA FILTRAR A BUSCA!")


    def main(self):
        while True:
            op = self.view.menu_view_principal()
            if op == 1:
                self.estoque_controller_insert()
            elif op == 2:
                    self.estoque_controller_list()
            elif op == 3:
                    self.estoque_controller_update()
            elif op == 4:
                    self.estoque_controller_delete()
            elif op == 5:
                    self.controller_vendas.vendas_controller_input()
            elif op == 6:
                    self.controller_vendas.relatorio_vendas()
            elif op == 7:
                    self.controller_vendas.relatorio_geral()
            elif op == 8:
                    self.buscar()
            elif op == 321:
                    self.estoque_controller_delete_all()
                    break
            elif op == 0:
                    self.view.estoque_response("FINISH PROGRAM!")
                    break