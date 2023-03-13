import os.path

import pygame as pg
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
TEAL = (0,255,255)
PURPLE = (128,0,255)

# Game title
TITLE = "Change me"

# Screen parameters
WIDTH = 500
HEIGHT = 500
DEFAULT_COLOR = BLACK

fps = 60
# file locations
game_folder = os.path.dirname(__file__)
game_folder = game_folder.replace("\scripts","")
sprites_folder = os.path.join(game_folder,"sprites")
player_sprites = os.path.join(sprites_folder,"player sprites")
enemies_sprites = os.path.join(sprites_folder,"enemies sprites")
print(game_folder)

# camera settings section


# player settings section
solid_bounds = False
bouncy = True
player_img_location = os.path.join(player_sprites,"dvd_logo.png")


# enemies settings section
enemy_img_location = os.path.join(enemies_sprites,"spike-ball.png")

