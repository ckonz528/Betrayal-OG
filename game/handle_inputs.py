from .graphics import Graphics
from .game import Game
import pygame
import game.settings as s


class HandleInputs:
    def __init__(self, game_info: Game, graphics: Graphics):
        self.game_info = game_info
        self.graphics = graphics

    def handle_input(self):

        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            self.game_info.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # place a tile
            mouse_x, mouse_y = pygame.mouse.get_pos()
            room = self.pick_room()
            if room == None:
                print('No more tiles available for this floor')
            else:
                self.game_info.floors[self.graphics.current_floor].place_tile(
                    room, (mouse_x // s.TILE_SIZE + self.graphics.camera[0], mouse_y // s.TILE_SIZE + self.graphics.camera[1]))

        if event.type == pygame.KEYDOWN:
            # move camera
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.graphics.camera = (
                    self.graphics.camera[0] - 1, self.graphics.camera[1])
            elif keys[pygame.K_RIGHT]:
                self.graphics.camera = (
                    self.graphics.camera[0] + 1, self.graphics.camera[1])
            elif keys[pygame.K_UP]:
                self.graphics.camera = (
                    self.graphics.camera[0], self.graphics.camera[1] - 1)
            elif keys[pygame.K_DOWN]:
                self.graphics.camera = (
                    self.graphics.camera[0], self.graphics.camera[1] + 1)

            # move player
            elif keys[pygame.K_a]:
                self.game_info.hero.pos = (
                    self.game_info.hero.pos[0] - 1, self.game_info.hero.pos[1])
            elif keys[pygame.K_d]:
                self.game_info.hero.pos = (
                    self.game_info.hero.pos[0] + 1, self.game_info.hero.pos[1])
            elif keys[pygame.K_w]:
                self.game_info.hero.pos = (
                    self.game_info.hero.pos[0], self.game_info.hero.pos[1] - 1)
            elif keys[pygame.K_s]:
                self.game_info.hero.pos = (
                    self.game_info.hero.pos[0], self.game_info.hero.pos[1] + 1)

            # exit
            elif keys[pygame.K_ESCAPE]:
                self.game_info.running = False

            # rotate tiles
            elif keys[pygame.K_n]:
                self.game_info.floor[self.graphics.current_floor].rotate_recent(
                    'left')
            elif keys[pygame.K_m]:
                self.game_info.floors[self.graphics.current_floor].rotate_recent(
                    'right')

            # switch floors
            elif keys[pygame.K_u]:
                self.graphics.current_floor = 'upper'
                self.graphics.camera = (0, 0)
            elif keys[pygame.K_g]:
                self.graphics.current_floor = 'ground'
                self.graphics.camera = (0, 0)
            elif keys[pygame.K_b]:
                self.graphics.current_floor = 'basement'
                self.graphics.camera = (0, 0)

    # TODO: move to a separate logic class
    def pick_room(self):
        if self.graphics.current_floor == 'basement':
            floor = 1
        elif self.graphics.current_floor == 'ground':
            floor = 2
        elif self.graphics.current_floor == 'upper':
            floor = 4

        for i, room_name in enumerate(self.game_info.room_keys):
            if self.game_info.rooms[room_name].floors & floor:
                room = self.game_info.rooms[room_name]
                del self.game_info.room_keys[i]
                return room
        return None
