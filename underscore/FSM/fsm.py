# Finite State Machine

class State:
    def enter(self, **kwargs):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def handle_input(self, user_input):
        pass

class FSM:
    def __init__(self):
        self.states = {}
        self.current = None

    def register(self, name, state_obj):
        self.states[name] = state_obj

    def change(self, name, **kwargs):
        if self.current:
            self.current.exit()
        self.current = self.states.get(name)
        if self.current:
            self.current.enter(**kwargs)

    def update(self):
        if self.current:
            self.current.update()

    def render(self):
        if self.current:
            self.current.render()

    def handle_input(self, user_input):
        if self.current:
            return self.current.handle_input(user_input)