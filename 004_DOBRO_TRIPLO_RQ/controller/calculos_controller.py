from math import sqrt
from model.calculos_model import CalculosModel
from view.calculos_view import CalculosView

class CalculosController:
    def __init__(self):
        self.calculos_model = CalculosModel()
        self.calculos_view = CalculosView(self)

    def calculos_controller(self):
        try:
            numero = self.calculos_view.calculos_view_numero()
            dobro = int(numero) * 2
            triplo = int(numero) * 3
            rq = sqrt(int(numero))
            self.calculos_model.calculos_insert(numero, dobro, triplo, rq)
        except ValueError: self.calculos_view.message("\nERRO: DIGITE UM NUMERO INTEIRO!\n")

    def calculos_calculos_response(self):
        view = self.calculos_model.calculos_list()
        for column in view:
            self.calculos_view.message(f"""
O DOBRO DE {column[1]} É {column[2]}

O TRIPLO DE {column[1]} É {column[3]}

A RAIZ QUADRADA DE {column[1]} É {column[4]}
""")