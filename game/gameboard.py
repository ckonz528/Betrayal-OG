import pygame
from pygame import locals
from pygame.sprite import Sprite
import game.settings as s


class Tile(Sprite):
    def __init__(self, tile_info):
        self.name = tile_info['name']
        self.doors = [d in tile_info['doors'] for d in 'NESW']
        self.card = tile_info['card']
        self.floors = tile_info['floors']

        # construct image file name
        img = self.name.lower().replace(' ', '_').replace("'", '')

        self.surf = pygame.image.load(s.get_path(
            'assets', f'images/rooms/{img}.png')).convert()
        self.surf = pygame.transform.scale(
            self.surf, (s.TILE_SIZE, s.TILE_SIZE))

    def rotate(self, direction):
        """Two things need to happen here:
        1. Change the elements in 'doors' so they correspond to the rotated tile
        2. Rotate the actual surface image so it can be drawn correctly"""
        assert direction in ('left', 'right')
        if direction == 'left':
            self.doors = self.doors[1:] + self.doors[:1]
            self.surf = pygame.transform.rotate(self.surf, -90)
        else:
            self.doors = self.doors[-1:] + self.doors[:-1]
            self.surf = pygame.transform.rotate(self.surf, 90)


class Gameboard:
    def __init__(self):
        self.tiles = {}
        self.players = []
        self.recent_pos = None

    def draw_board(self, screen, cam_pos=(0, 0)):
        tiles_across = s.WIDTH // s.TILE_SIZE
        tiles_down = s.HEIGHT // s.TILE_SIZE
        camx, camy = cam_pos

        # place tiles
        for xpos, ypos in self.tiles:
            tile = self.tiles[xpos, ypos]
            if 0 <= xpos - camx <= tiles_across and 0 <= ypos - camy <= tiles_down:
                screen.blit(tile.surf, ((xpos - camx) *
                                        s.TILE_SIZE, (ypos - camy) * s.TILE_SIZE))

        # display players
        for hero in self.players:
            xpos, ypos = hero.pos
            if 0 <= xpos - camx <= tiles_across and 0 <= ypos - camy <= tiles_down:
                screen.blit(hero.surf, ((xpos - camx) *
                                        s.TILE_SIZE, (ypos - camy) * s.TILE_SIZE))

    def place_tile(self, tile, pos):
        # TODO: add logic to check whether it is legal to place this tile here
        if pos in self.tiles:
            print('There is already a tile here.')
        else:
            self.tiles[pos] = tile
            self.recent_pos = pos

    def rotate_recent(self, direction):
        if self.recent_pos == None:
            pass
        else:
            self.tiles[self.recent_pos].rotate(direction)
