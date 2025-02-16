from datetime import datetime
from model.model_vendas import VendasModel
from model.model_estoque import EstoqueModel
from view.view import EstoqueView


class ControllerVendas:
    data_hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S-%p")

    def __init__(self):
        self.model_vendas = VendasModel()
        self.model_estoque = EstoqueModel()
        self.view = EstoqueView()


    def vendas_controller_input(self):
        try:
            self.view.estoque_response("$ MENU DE VENDAS $")
            estoque_id, quantidade = self.view.vendas_view_input()
            get = self.model_estoque.estoque_get_by_id(estoque_id)
            if get:
                produto = get[1]
                quant = get[2]
                preco = get[3]
                total = get[4]
                status = get[5]
                if quant >= status and quant >= quantidade:
                    calc_quant = quant - quantidade
                    calc_venda = quantidade * (preco * 210 / 100)
                    calc_total =  total - calc_venda
                    status = "EM ESTOQUE"
                    self.view.estoque_response("DETALHES DO PRODUTO A SER VENDIDO:")
                    self.view.estoque_view_list(get, status)
                    self.model_vendas.vendas_insert(estoque_id, produto, quantidade, calc_venda, self.data_hora)
                    if calc_total < 0:
                        calc_total = 0
                        self.model_vendas.update_estoque_by_vendas(calc_quant, calc_total, estoque_id)
                    self.view.estoque_response("$ PRODUTO VENDIDO COM SUCESSO $")
                    list_ = self.model_vendas.vendas_success()
                    self.view.relatorio_vendas(list_)
                else:
                    status = "SEM ESTOQUE - PARA ESSA VENDA"
                    self.view.estoque_response("ERRO: ESSE PRODUTO NÃO PODE SER VENDIDO, POIS NÃO TEMOS A\nQUANTIDADE EXIGIDA PARA A VENDA!")
                    self.view.estoque_response("DETALHES DO PRODUTO:")
                    self.view.estoque_view_list(get, status)
            else:
                self.view.estoque_response("ERRO: ID INEXISTENTE, DIGITE UM ID VALIDO!")
        except ValueError:
             self.view.estoque_response("ERRO: TODOS OS CAMPOS DEVEM SER PREENCHIDOS COM NUMEROS INTEIROS!")


    def relatorio_vendas(self):
        relatorio = self.model_vendas.vendas_read()
        self.view.estoque_response("$ RELATÓRIO DE VENDAS $")
        if relatorio:
            for lista in relatorio:
                self.view.relatorio_vendas(lista)
        else:
            self.view.estoque_response("ERRO: NÃO EXISTE REGISTRO DE VENDAS NO BANCO DE DADOS")


    def relatorio_geral(self):
        try_ = self.model_vendas.vendas_read()
        if try_:
            relatorio = self.model_vendas.relatorio_geral()
            self.view.estoque_response("$RELATÓRIO - FINANCEIRO - GERAL")
            self.view.relatorio_geral(relatorio, self.data_hora)
        else:
            self.view.estoque_response("SEM REGISTROS PARA GERAR UM RELATÓRIO NO MOMENTO!")