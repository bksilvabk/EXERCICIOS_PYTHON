from controller.somar_controller import SomarController

__name__ == "__main__"

controller = SomarController()
while True:
    controller.somar_controller_input()

    exit = str(input("\nEXIT? y/n: ")).strip().upper()
    if exit == "Y": 
        print("\nFINISH PROGRAM!") 
        break