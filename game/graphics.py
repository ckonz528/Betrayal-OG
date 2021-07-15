from game.game import Game
import pygame
from typing import Tuple
import game.settings as s


class Graphics:
    def __init__(self, game_info: Game):
        self.game_info = game_info
        self.current_floor: str = 'ground'
        self.camera: Tuple[int, int] = (0, 0)

    def draw_to(self, screen: pygame.Surface):
        screen.fill(s.WHITE)
        self.game_info.floors[self.current_floor].draw_board(
            screen, self.camera)
        pygame.display.flip()
