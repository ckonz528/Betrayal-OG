import pygame
import json
import game.settings as s
from .gameboard import Tile, Gameboard
import random as r


class Betrayal:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption(s.TITLE)

        # load tiles
        tiles = json.load(open(s.get_path('assets', 'data/rooms.json')))
        self.rooms = [Tile(room_info) for room_info in tiles]

        # create floors
        self.ground = Gameboard()

        self.camera = (0, 0)
        
        self.redraw()

    def run_game(self):
        running = True
        while running:
            redraw_needed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    room = self.pick_room()
                    self.ground.place_tile(room, (mouse_x // s.TILE_SIZE + self.camera[0], mouse_y // s.TILE_SIZE + self.camera[1]))
                    redraw_needed = True
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        self.camera = (self.camera[0] - 1, self.camera[1])
                        redraw_needed = True
                    elif keys[pygame.K_RIGHT]:
                        self.camera = (self.camera[0] + 1, self.camera[1])
                        redraw_needed = True
                    elif keys[pygame.K_UP]:
                        self.camera = (self.camera[0], self.camera[1] - 1)
                        redraw_needed = True
                    elif keys[pygame.K_DOWN]:
                        self.camera = (self.camera[0], self.camera[1] + 1)
                        redraw_needed = True
            if redraw_needed:
                self.redraw()
        pygame.quit()

    def redraw(self):
        self.screen.fill(s.WHITE)
        self.ground.draw_board(self.screen, self.camera)
        pygame.display.flip()

    def pick_room(self):
        return r.choice(self.rooms)
