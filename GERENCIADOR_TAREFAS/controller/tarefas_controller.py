from model.tarefas_model import TarefasModel
from view.tarefas_view import TarefasView

class TarefasController:

    def __init__(self):
        self.model = TarefasModel()
        self.view = TarefasView(self)


    def tarefas_input_insert(self):
        _input = self.view.tarefa_input().strip().capitalize()
        if _input != "":
            self.model.tarefas_insert(_input)
            self.view.tarefa_response("Tarefa registrada com sucesso. Para ver a tarefa basta ir no menu (LISTAR)\n\n")
        else: 
            self.view.tarefa_response("\nDigite uma tarefa valida")


    def tarefas_list_read(self):
        self.view.tarefa_response("\n\nTAREFAS SALVAS:")
        _list = self.model.tarefas_read()
        if not _list:
            self.view.tarefa_response("Nenhuma tarefa encontrada, crie uma nova tarefa no menu (CRIAR)!\n\n")
        else:
            self.view.tarefa_list(_list)
                        

    def tarefas_update(self):
        try:
            update = self.view.tarefas_update()
            id = self.model.get_by_id(update)
            if id and  isinstance(update, int):
                tarefa = self.view.tarefa_input()
                if tarefa != "":
                    self.model.tarefas_update(tarefa, update)
                    get = self.model.get_by_id(update)
                    self.view.tarefa_list_update(get)
            else:
                self.view.tarefa_response("ERRO: TENTE NOVAMENTE EM INSTANTES!")
        except ValueError: self.view.tarefa_response("\nERRO: ID INVÁLIDO!")


    def tarefas_update_status(self):
        try:
            id = self.view.tarefas_update()
            status = self.view.tarefas_update_status()
            _get = self.model.get_by_id(id)
            for up in _get:
                self.model.tarefas_update_status(status, id)
                self.view.tarefa_response("STATUS ATERADO COM SUCESSO!")
        except ValueError: self.view.tarefa_response("ERRO: ALGO DEU ERRADO, TENTE NOVAMENTE!\n")




    def tarefas_delete(self):
        try:
            delete = self.view.tarefas_delete()
            id = self.model.get_by_id(delete)
            if id:
                self.model.tarefas_delete(delete)
                self.view.tarefa_response(f"\nTAREFA {delete} - deletada com sucesso!")
            else:
                self.view.tarefa_response("\nID não existe, use a lista de tarefas para facilitar sua busca!")
        except ValueError: self.view.tarefa_response("\nERRO: ID NÃO INVÁLIDO!")



    def main(self):
        op = True
        while op != False:
            try:
                op = self.view.tarefas_menu()
                if isinstance(op, int):
                    if op == 0:
                        op = False
                        self.view.tarefa_response("\n\nFINISH PROGRAM!\n\n")
                    if op == 1:
                        self.tarefas_input_insert()
                    elif op == 2:
                        self.tarefas_list_read()
                    elif op == 3:
                        up = int(input("\nAlterar TAREFA - 1, Alterar STATUS - 0: "))
                        if up == 1:
                            self.tarefas_update()
                        elif up == 0:
                            self.tarefas_update_status()
                    elif op == 4:
                        self.tarefas_delete()
                    elif op == 000:
                        self.model.tarefas_delete_all()
                        self.model.drop_table()
            except ValueError:
                self.view.tarefa_response("\nERRO: SELECIONE UMA DAS OPÇÕES A BAIXO!")