import pygame
from pygame import locals
from pygame.sprite import Sprite
import game.settings as s


class Player(Sprite):
    def __init__(self, player_info):
        # player stats
        self.name = player_info['name']
        self.speed_bar = player_info['speed']
        self.might_bar = player_info['might']
        self.sanity_bar = player_info['sanity']
        self.knowledge_bar = player_info['knowledge']

        # set inital position
        self.pos = (4, 1)

        # set base attribute levels
        self.base = player_info['base']

        self.speed = self.speed_bar[self.base[0]]
        self.might = self.might_bar[self.base[1]]
        self.sanity = self.sanity_bar[self.base[2]]
        self.knowledge = self.knowledge_bar[self.base[3]]

        # construct image file name
        img = self.name.lower().replace(' ', '_').replace("'", '')

        self.surf = pygame.image.load(s.get_path(
            'assets', f'images/players/{img}.png')).convert()
        self.surf = pygame.transform.scale(
            self.surf, (s.PLAYER_SIZE, s.PLAYER_SIZE))
