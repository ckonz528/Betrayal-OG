import pygame
import json
from . import settings as s
from .gameboard import Tile, Gameboard
import random as r


class Betrayal:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption(s.title)

        # load tiles
        tiles = json.load(open('assets/data/rooms.json'))
        self.rooms = [Tile(room_info) for room_info in tiles]

        # create floors
        self.ground = Gameboard()

    def run_game(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    room = self.pick_room()
                    self.ground.place_tile(room, (0, 0))

            self.screen.fill(s.WHITE)
            self.ground.draw_board(self.screen)
            pygame.display.flip()

        pygame.quit()

    def pick_room(self):
        return r.choice(self.rooms)
