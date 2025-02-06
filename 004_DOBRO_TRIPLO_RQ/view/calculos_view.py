class CalculosView:
    def __init__(self, controller):
        self.controller = controller

    def message(self, message): print(message)

    def calculos_view_numero(self):
        numero = str(input("\nDigite um numero: "))
        return numero