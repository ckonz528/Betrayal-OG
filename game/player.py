import pygame
from pygame import locals
from pygame.sprite import Sprite
import game.settings as s


class Player(Sprite):
    def __init__(self, player_info):
        # player stats
        self.name = player_info['name']

        # set inital position on floor
        self.pos = (4, 1)

        # set base attribute levels
        self.base = player_info['base']

        # Player stats as dictionary
        self.stats = {'speed': (player_info['speed'], self.base[0]),
                      'might': (player_info['might'], self.base[1]),
                      'sanity': (player_info['sanity'], self.base[2]),
                      'knowledge': (player_info['knowledge'], self.base[3])}

        self.items = []

        # construct image file name
        img = self.name.lower().replace(' ', '_').replace("'", '')

        self.surf = pygame.image.load(s.get_path(
            'assets', f'images/players/{img}.png')).convert()
        self.surf = pygame.transform.scale(
            self.surf, (s.PLAYER_SIZE, s.PLAYER_SIZE))

    def move_player(self):
        pass

    def raise_stat(self, stat, num_levels):
        self.stats[stat] = (self.stats[stat][0],
                            self.stats[stat][1] + num_levels)

        # check for upper bound
        if self.stats[stat][1] >= len(self.stats[stat][0]):
            self.stats[stat] = (self.stats[stat][0], 8)

    def lower_stat(self, stat, num_levels):
        self.stats[stat] = (self.stats[stat][0],
                            self.stats[stat][1] - num_levels)

        # check for death/ lower bound
        if self.stats[stat][1] <= 0:
            # TODO: write death protocol/ check if haunt mode
            pass

    def physical_damage(self, num_levels):
        while num_levels > 0:
            # TODO: make this more resilient to input errors
            print('Choose which stat to lower by one level:')
            print('\t1 - Speed')
            print('\t2 - Might')

            stat_choice = int(input('Your choice: '))

            if stat_choice not in [1, 2]:
                print('Invalid choice. Please enter only 1 or 2.')
            elif stat_choice == 1:
                self.lower_stat('speed', 1)
                num_levels -= 1
            else:
                self.lower_stat('might', 1)
                num_levels -= 1

    def mental_damage(self, num_levels):
        while num_levels > 0:
            # TODO: make this more resilient to input errors
            print('Choose which stat to lower by one level:')
            print('\t1 - Sanity')
            print('\t2 - Knowledge')

            stat_choice = int(input('Your choice: '))

            if stat_choice not in [1, 2]:
                print('Invalid choice. Please enter only 1 or 2.')
            elif stat_choice == 1:
                self.lower_stat('sanity', 1)
                num_levels -= 1
            else:
                self.lower_stat('knowledge', 1)
                num_levels -= 1

    def display_stats(self):
        pass
