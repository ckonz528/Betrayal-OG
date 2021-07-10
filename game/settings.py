import os
BASE_PATH = os.getcwd()


def get_path(folder, file): return os.path.join(BASE_PATH, folder, file)


# display settings
WIDTH = 1000
HEIGHT = 600

TITLE = 'Betrayal at House on a Hill'

# image sizes
TILE_SIZE = 200
PLAYER_SIZE = 75

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
