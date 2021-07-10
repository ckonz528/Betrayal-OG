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
        self.rooms: dict[str, Tile] = {room_info['name']: Tile(
            room_info) for room_info in tiles}

        # create floors
        self.floors = {'ground': Gameboard(), 'basement': Gameboard(),
                       'upper': Gameboard()}

        # add starting tiles
        start_tiles = [(4, 'Entrance Hall'), (3, 'Foyer'),
                       (2, 'Grand Staircase')]
        for x, room in start_tiles:
            self.floors['ground'].place_tile(self.rooms[room], (x, 1))
            del self.rooms[room]

        self.floors['upper'].place_tile(self.rooms['Upper Landing'], (2, 1))
        del self.rooms['Upper Landing']

        self.floors['basement'].place_tile(
            self.rooms['Basement Landing'], (2, 1))
        del self.rooms['Basement Landing']

        # disable rotation for all floors
        for floor in list(self.floors.keys()):
            self.floors[floor].recent_pos = None

        # set current floor
        self.current_floor = 'ground'

        # shuffle list of tiles
        self.room_keys: list[str] = list(self.rooms.keys())
        r.shuffle(self.room_keys)

        # place camera in starting position
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
                    if room == None:
                        # TODO: add log for messages
                        print('No more tiles available for this floor.')
                    else:
                        self.floors[self.current_floor].place_tile(
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
                        self.floors[self.current_floor].rotate_recent('left')
                        redraw_needed = True
                    elif keys[pygame.K_m]:
                        self.floors[self.current_floor].rotate_recent('right')
                        redraw_needed = True

                    # switch floors
                    elif keys[pygame.K_u]:
                        self.current_floor = 'upper'
                        self.camera = (0, 0)
                        redraw_needed = True
                    elif keys[pygame.K_g]:
                        self.current_floor = 'ground'
                        self.camera = (0, 0)
                        redraw_needed = True
                    elif keys[pygame.K_b]:
                        self.current_floor = 'basement'
                        self.camera = (0, 0)
                        redraw_needed = True

            if redraw_needed:
                self.redraw()
        pygame.quit()

    def redraw(self):
        self.screen.fill(s.WHITE)
        self.floors[self.current_floor].draw_board(self.screen, self.camera)
        pygame.display.flip()

    def pick_room(self):
        if self.current_floor == 'basement':
            floor = 1
        elif self.current_floor == 'ground':
            floor = 2
        elif self.current_floor == 'upper':
            floor = 4

        for i, room_name in enumerate(self.room_keys):
            if self.rooms[room_name].floors & floor:
                room = self.rooms[room_name]
                del self.room_keys[i]
                return room
        return None
