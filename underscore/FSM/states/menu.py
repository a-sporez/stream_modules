from fsm import State

class MenuState(State):
    def enter(self, **kwargs):
        print("Menu Loaded")

    def handle_input(self, user_input):
        if user_input == "start":
            return 'running'
        elif user_input == "quit":
            return 'quit'
        
    def update(self):
        pass

    def render(self):
        print("[menu] Type 'start' or 'quit'")