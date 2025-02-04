class Print:
    def __init__(self, controller):
        self.controller = controller

    def print_view(self, message): print(f'''\nHello {message}, nice to meet you <3\n\n''')
    print('''\n\nDESAFIO 0.1: FAZER UM INPUT() PARA PEGAR O NOME DO USUÁRIO E
MOSTRE UMA MENSAGEM DE CORTESIA!

EXECUÇÃO SIMPLES:
nome = str(input('Digite seu nome:'))
print('Olá ', nome, ' prazer em conhece-lo!')

OBS: EXECUÇÃO EM UMA ESTRUTURA MVC A SEGUIR: \n
              ''')