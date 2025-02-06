from model.somar_model import SomarModel
from view.somar_view import SomarView

class SomarController:
    def __init__(self):
        self.somar_db = SomarModel()
        self.somar_view = SomarView(self)

    def somar_controller_input(self):
        v1 = str(input("\nDigite um numero: ")).strip()
        v2 = str(input("\nDigite outro numero: ")).strip()
        try:
            self.somar_db.somar_insert(int(v1))
            self.somar_db.somar_insert(int(v2))
            response = self.somar_db.somar_list()
            if len(response) == 2:
                v1, v2 = response[0][0], response[1][0]
                soma = v1 + v2
                self.somar_view.somar_view_print(f"\nA soma entre {v1} e {v2} é igual a {soma}\n\n")
        except ValueError: self.somar_view.somar_view_print("\nERRO: Digite numeros inteiros para seguir!")