from fsm import State

class IntroState(State):
    def enter(self, **kwargs):
        print("Intro loaded")

    def handle_input(self, user_input):
        if user_input.lower() == "continue":
            return 'menu'
        
    def update(self):
        pass

    def render(self):
        print("[intro] type 'continue' to proceed.")