from view.print_view import Print
from model.print_model import DataBase

class PrintController:
    def __init__(self):
        self.print_view = Print(self)
        self.db = DataBase()

    def runing(self):
        people = str(input("\nYour name:")).upper()
        self.db.people_insert(people)

    def response_controller(self):
        response = self.db.response_model()
        self.print_view.print_view(response)