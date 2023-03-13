import os.path

import pygame as pg
import random

debugging = True

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
TEAL = (0,255,255)
PURPLE = (128,0,255)
PINK = (255,150,255)
CORN_FLOWER_BLUE = (100,149,237)

# Game title
TITLE = "SHMUP (BEST GAME EVER)"

# Screen parameters
WIDTH = 650
HEIGHT = 1000
DEFAULT_COLOR = BLACK

fps = 40
# file locations
game_folder = os.path.dirname(__file__)
game_folder = game_folder.replace("\scripts","")
sprites_folder = os.path.join(game_folder,"sprites")
player_folder = os.path.join(sprites_folder,"player sprites")
enemy_folder = os.path.join(sprites_folder,"enemies sprites")
background_folder = os.path.join(sprites_folder,"backgrounds")
explosion_folder = os.path.join(sprites_folder,"explosions")
power_up_folder = os.path.join(sprites_folder,"power ups")
bullets_folder = os.path.join(sprites_folder,"bullets")

bg_images = ["Space_BG_01.png","Space_BG_02.png","Space_BG_03.png","Space_BG_04.png",]
bg_img = random.choice(bg_images)



print(game_folder)

# camera settings section


# player settings section
solid_bounds = True
move_speed = 12
player_w = 65
player_h = 65

player_img_location = "Ship_04.png"
bullet_img = "Missile.png"
bullet_w = 10
bullet_h = 20


# enemies settings section


