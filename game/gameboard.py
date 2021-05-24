import pygame
from pygame.sprite import Sprite
import game.settings as s


class Tile(Sprite):
    def __init__(self, tile_info):
        self.name = tile_info['name']
        self.doors = tile_info['doors']
        self.card = tile_info['card']
        self.floors = tile_info['floors']

        # construct image file name
        img = self.name.lower().replace(' ', '_').replace("'", '')

        self.surf = pygame.image.load(s.get_path('assets', f'images/rooms/{img}.png')).convert()
        self.surf = pygame.transform.scale(
            self.surf, (s.TILE_SIZE, s.TILE_SIZE))


class Gameboard:
    def __init__(self):
        self.tiles = []

    def draw_board(self, screen, cam_pos=(0, 0)):
        tiles_across = s.WIDTH // s.TILE_SIZE
        tiles_down = s.HEIGHT // s.TILE_SIZE
        camx, camy = cam_pos
        for tile, (xpos, ypos) in self.tiles:
            if 0 <= xpos - camx <= tiles_across and 0 <= ypos - camy <= tiles_down:
                screen.blit(tile.surf, ((xpos - camx) * s.TILE_SIZE, (ypos - camy) * s.TILE_SIZE))

    def place_tile(self, tile, pos):
        self.tiles.append((tile, pos))
