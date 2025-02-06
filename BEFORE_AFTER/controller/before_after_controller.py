from model.before_after_model import BeforAfterModel
from view.before_after_view import BeforeAfterView

class BeforeAfterController:
    def __init__(self):
        self.before_after_model = BeforAfterModel()
        self.before_after_view = BeforeAfterView(self)

    def before_after_controller(self):
        numero = str(input("\nDigite um numero: ")).strip()
        try:
            self.before_after_model.before_after_insert(int(numero))
            response = self.before_after_model.before_after_list()
            if response is not None:
                self.before_after_view.before_after_view(f"\nO antecessor de {response} é {response - 1}, e seu sucessor é {response + 1}")
        except ValueError: self.before_after_view.before_after_view("\nERRO: Digite apenas numeros inteiros!\n")