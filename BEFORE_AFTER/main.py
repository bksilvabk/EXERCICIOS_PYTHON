from controller.before_after_controller import BeforeAfterController

__name__ == "__main__"

controller = BeforeAfterController()
while True:
    controller.before_after_controller()
    exit = str(input("\nEXIT? y/n: ")).strip().upper()
    if exit == "Y": 
        print("\nFINISH PROGRAM!") 
        break