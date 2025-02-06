from controller.calculos_controller import CalculosController

__name__ == "__main__"

controller = CalculosController()
while True:
    controller.calculos_controller()
    controller.calculos_calculos_response()
    exit = str(input("\nEXIT? y/n: ")).strip().upper()
    if exit == "Y": 
        print("\nFINISH PROGRAM!") 
        break