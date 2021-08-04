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

    def change_stat(self, stat, num_levels=1):
        '''
        Alters a player's stat value

        stat (str): a string of the stat that is to change (speed, might, knowledge, sanity)
        num_levels (int): number of levels the stat will change; positive for increase, negative for decreas
        '''
        self.stats[stat] = (self.stats[stat][0],
                            self.stats[stat][1] + num_levels)

        # check for upper bound
        if self.stats[stat][1] >= len(self.stats[stat][0]):
            self.stats[stat] = (self.stats[stat][0], 8)

        # check for death/ lower bound
        if self.stats[stat][1] <= 0:
            # TODO: write death protocol/ check if haunt mode
            pass

    def change_physical(self, num_levels):
        changes = abs(num_levels)

        while changes > 0:
            # TODO: make this more resilient to input errors
            print('Choose which physical stat to change by one level:')
            print('\t1 - Speed')
            print('\t2 - Might')

            stat_choice = int(input('Your choice: '))

            if stat_choice not in [1, 2]:
                print('Invalid choice. Please enter only 1 or 2.')
            elif stat_choice == 1:
                self.change_stat('speed', int(num_levels/abs(num_levels)))
                changes -= 1
            else:
                self.change_stat('might', int(num_levels/abs(num_levels)))
                changes -= 1

    def change_mental(self, num_levels):
        changes = abs(num_levels)

        while changes > 0:
            # TODO: make this more resilient to input errors
            print('Choose which mental stat to change by one level:')
            print('\t1 - Sanity')
            print('\t2 - Knowledge')

            stat_choice = int(input('Your choice: '))

            if stat_choice not in [1, 2]:
                print('Invalid choice. Please enter only 1 or 2.')
            elif stat_choice == 1:
                self.change_stat('sanity', int(num_levels/abs(num_levels)))
                changes -= 1
            else:
                self.change_stat('knowledge', int(num_levels/abs(num_levels)))
                changes -= 1

    def display_stats(self):
        print(f'Current stats for {self.name}:')
        print(f'\tSpeed: {self.stats["speed"][0][self.stats["speed"][1]]}')
        print(f'\tMight: {self.stats["might"][0][self.stats["might"][1]]}')
        print(f'\tSanity: {self.stats["sanity"][0][self.stats["sanity"][1]]}')
        print(
            f'\tKnowledge: {self.stats["knowledge"][0][self.stats["knowledge"][1]]}')
