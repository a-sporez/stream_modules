# main endpoint for testing
# I guessed the module import, still not familiar with python file structure.
from fsm import FSM
from states.intro import IntroState
from states.menu import MenuState
from states.running import RunningState

def main():
    # Register states and load intro.
    fsm = FSM()
    fsm.register('intro', IntroState())
    fsm.register('menu', MenuState())
    fsm.register('running', RunningState())

    fsm.change('intro')

    while True:
        fsm.render()
        user_input = input('> ')
        if user_input == 'quit':
            break
        next_state = fsm.handle_input(user_input)
        print(f"[debug-main] handle_input() returns: {next_state}")
        
        if isinstance(next_state, str):
            if next_state == 'quit':
                break
            fsm.change(next_state)
        fsm.update()

if __name__ == '__main__':
    main()