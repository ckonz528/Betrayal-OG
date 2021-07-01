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
        self.rooms = {room_info['name']: Tile(
            room_info) for room_info in tiles}

        # create floors
        self.ground = Gameboard()
        self.ground.place_tile(self.rooms['Entrance Hall'], (4, 1))
        self.ground.place_tile(self.rooms['Foyer'], (3, 1))
        self.ground.place_tile(self.rooms['Grand Staircase'], (2, 1))
        self.ground.recent_pos = None

        self.camera = (0, 0)
        self.running = True
        self.redraw()

    def run_game(self):
        while self.running:
            redraw_needed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # place tiles
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    room = self.pick_room()
                    self.ground.place_tile(
                        room, (mouse_x // s.TILE_SIZE + self.camera[0], mouse_y // s.TILE_SIZE + self.camera[1]))
                    redraw_needed = True

                # key down event listeners
                if event.type == pygame.KEYDOWN:
                    # move camera
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

                    # exit game on esc
                    elif keys[pygame.K_ESCAPE]:
                        self.running = False

                    # rotate tiles
                    elif keys[pygame.K_n]:
                        self.ground.rotate_recent('left')
                        redraw_needed = True
                    elif keys[pygame.K_m]:
                        self.ground.rotate_recent('right')
                        redraw_needed = True
            if redraw_needed:
                self.redraw()
        pygame.quit()

    def redraw(self):
        self.screen.fill(s.WHITE)
        self.ground.draw_board(self.screen, self.camera)
        pygame.display.flip()

    def pick_room(self):
        room = r.choice(list(self.rooms.keys()))
        return self.rooms[room]
