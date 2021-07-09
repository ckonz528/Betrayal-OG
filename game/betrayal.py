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
        '''make a dictionary of floors
           have a string that tracks current floor (self.current_floor)
           replace self.ground with self.floors['ground'] or self.floors[self.current_floor]
           place starting tiles
           add logic for keys to switch floors (b,g,u)
        '''
        self.ground = Gameboard()
        start_tiles = ['Entrance Hall', 'Foyer', 'Grand Staircase']
        x = 4
        for room in start_tiles:
            self.ground.place_tile(self.rooms[room], (x, 1))
            x -= 1
            del self.rooms[room]
        self.ground.recent_pos = None

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
        for i, room_name in enumerate(self.room_keys):
            if self.rooms[room_name].floors == 2:
                room = self.rooms[room_name]
                del self.room_keys[i]
                return room
        return None
