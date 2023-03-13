import pygame as pg
from xboxController import *

TITLE = "Crossy Guy"

WIDTH = 800
HEIGHT = 1000

tile_size = HEIGHT/20

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cyan = (0,255,255)
purple = (150,0,255)

fps = 40

bgimg_location = "sprites/background.png"
trimg_location = "sprites/treasure.png"
player_img = "sprites/player.png"
enemy_img = "sprites/enemy.png"
enemy2_img = "sprites/enemy2.png"
diamond_img = "sprites/diamond.png"

# player settings
player_start_pos_x = WIDTH//2-tile_size//2
player_start_pos_y = HEIGHT-tile_size
player_speed = 10
sprint_mod = 2

# enemy settings
enemy_speed = 100
