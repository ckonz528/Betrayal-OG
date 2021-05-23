import pygame
from pygame.sprite import Sprite
import settings as s


class Tile(Sprite):
    def __init__(self, tile_info):
        self.name = tile_info['name']
        self.doors = tile_info['doors']
        self.card = tile_info['card']
        self.floors = tile_info['floors']

        # construct image file name
        img = self.name.lower().replace(' ', '_').replace("'", '')

        self.surf = pygame.image.load(
            f'../assets/images/rooms/{img}.png').convert()
        self.surf = pygame.transform.scale(
            self.surf, (s.TILE_SIZE, s.TILE_SIZE))


class Gameboard:
    def __init__(self):
        self.tiles = []

    def draw_board(self, screen, cam_pos=(0, 0)):
        for tile, pos in self.tiles:
            screen.blit(tile.surf, (0, 0))

    def place_tile(self, tile, pos):
        self.tiles.append((tile, pos))
