from game import MAIN_WINDOW
from .game import Game
from .graphics import Graphics
from .handle_inputs import HandleInputs

if __name__ == '__main__':
    game_info = Game()
    graphics = Graphics(game_info)
    input_handler = HandleInputs(game_info, graphics)

    while game_info.running:
        graphics.draw_to(MAIN_WINDOW)
        input_handler.handle_input()

    # betrayal = Betrayal()
    # betrayal.run_game()
