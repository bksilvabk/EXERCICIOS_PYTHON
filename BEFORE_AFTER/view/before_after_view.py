class BeforeAfterView:
    def __init__(self, controller):
        self.controller = controller

    def before_after_view(self, response): print(response)