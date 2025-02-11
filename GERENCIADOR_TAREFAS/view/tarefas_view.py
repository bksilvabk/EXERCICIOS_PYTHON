class TarefasView:

    def __init__(self, controller):
        self.controller = controller


    def tarefas_menu(self):
        op = int(input("""
***GERENCIADOR DE TAREFAS***
[1]CRIAR - Tarefa
[2]LISTAR - Tarefa
[3]EDITAR - Tarefa
[4]EXCLUIR - Tarefa
[123]EXCLUIR - TUDO
[0]SAIR

ESCOLHA: """))
        return op


    def tarefa_response(self, response): print(response)


    def tarefa_input(self):
        tarefa = str(input("\n\nDigite sua tarefa: "))
        return tarefa


    def tarefa_list(self, __list):
            for lista in __list:
                if lista[2] == 1:
                    status = "Concluido"
                if lista[2] == 0:
                    status = "Pendente"
                print(f"""
ID:{lista[0]} - TAREFA: {lista[1]}
STATUS: {status}
\n""")
            return

    def tarefa_list_update(self, _listar):
        print(f"""\nATUALIZAÇÃO CONCLUIDA COM SUCESSO! DETALHES:
ID:{_listar[0]} - TAREFA: {_listar[1]}
STATUS: {_listar[2]}
\n\n""")
        return


    def tarefas_update(self):
        id = int(input("\n\nDigite o id da tarefa a ser alterada: "))
        return id
    
    def tarefas_update_status(self):
        status = int(input("STATUS - 0-pendente, 1-concluido: "))
        return status


    def tarefas_delete(self):
        id = int(input("\n\nDigite o id da tarefa a ser deletada: "))
        return id