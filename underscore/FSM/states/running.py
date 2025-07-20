from fsm import State

class RunningState(State):
    def enter(self, **kwargs):
        print("Running state initialized. V2")

    def handle_input(self, user_input):
        if user_input == "menu":
            return 'menu'
        
    def update(self):
        pass

    def render(self):
        print("[running] Type 'menu' to go back.")