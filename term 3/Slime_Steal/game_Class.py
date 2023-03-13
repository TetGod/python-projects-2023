import random

from settings import *
from game_Objects import *


def draw_Text(screen, text, size, x, y, color):
    font_name = pg.font.match_font("impact")
    font = pg.font.Font(font_name, size)
    text_sprite = font.render(text, True, color)
    text_rect = text_sprite.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_sprite, text_rect)

class Game():

    def __init__(self):
        self.playing = True
        self.level = 0
        self.game_window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        joystick_count = pg.joystick.get_count()

        # set up controller if one is connected
        if joystick_count > 0:
            self.xbox_controller = Controller()
        else:
            self.xbox_controller = None

        self.background_img = GameObject(0, 0, WIDTH, HEIGHT, bgimg_location)
        self.treasure_img = GameObject(WIDTH / 2 - tile_size / 2, tile_size / 3, tile_size, tile_size, trimg_location)
        self.player = Player(player_start_pos_x, player_start_pos_y, tile_size, tile_size, player_img, player_speed)
        self.hasDiamond = True
        self.oneup_x = 1000
        self.oneup_y = 0



        self.extralife = GameObject(self.oneup_x,self.oneup_y,tile_size, tile_size, diamond_img)

        self.nextLevel()

    def start_game_loop(self):
        while self.playing:
            # tick Clock
            self.clock.tick(fps)
            # get inputs
            self.get_inputs()
            # update
            self.update()
            # draw
            self.draw()

    def get_inputs(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.playing = False
        self.get_player_inputs(events)

    def update(self):
        """ called in the game loop and updates all game objects"""
        self.player.move()

        for enemy in self.enemies_list:
            enemy.move(WIDTH)

        if self.detect_Collisions(self.player, self.treasure_img):
            self.player.collect()
            self.treasure_img.collect()
        if self.detect_Collisions(self.player, self.extralife):
            self.extralife.x+=1000
            self.player.lives += 1
            print(self.player.collected)

        for enemy in self.enemies_list:
            if self.detect_Collisions(self.player, enemy):
                self.player.x += 500
                self.player.die()
                if self.player.lives > 0:
                    self.resetLevel()
                else:
                    self.playing = False

        if self.player.collected and self.player.x < HEIGHT - 100:
            print("you win")
            self.nextLevel()

    def draw(self):
        self.game_window.fill(purple)
        self.game_window.blit(self.background_img.image, (self.background_img.x, self.background_img.y))
        self.game_window.blit(self.treasure_img.image, (self.treasure_img.x, self.treasure_img.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.extralife.image,(self.extralife.x,self.extralife.y))

        for enemy in self.enemies_list:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
            # self.game_window.blit(enemy2_img.image, (enemy2_img.x, enemy2_img.y))

        pg.display.update()

    def get_player_inputs(self, events):
        if self.xbox_controller:
            # hat = self.xbox_controller.get_hat()
            # self.player.set_move_dir(hat.get("H_X"), hat.get("H_Y"))

            get_axis = self.xbox_controller.get_axes()
            self.player.set_move_dir(get_axis.get("l_JOY_X"), get_axis.get("r_JOY_Y"))

            button_inputs = self.xbox_controller.get_buttons()
            a = button_inputs.get("CONT_A")

            if a > 0:
                self.player.sprint()
            else:
                self.player.walk()
        else:
            for event in events:

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w or event.key == pg.K_UP:
                        self.player.set_move_dir(0, -1)
                    if event.key == pg.K_s or event.key == pg.K_DOWN:
                        self.player.set_move_dir(0, 1)
                    if event.key == pg.K_a or event.key == pg.K_LEFT:
                        self.player.set_move_dir(-1, 0)

                    if event.key == pg.K_d or event.key == pg.K_RIGHT:
                        self.player.set_move_dir(1, 0)
                    if event.key == pg.K_RSHIFT or event.key == pg.K_LSHIFT:
                        self.player.sprint()

                if event.type == pg.KEYUP:
                    if event.key == pg.K_w or event.key == pg.K_UP or event.key == pg.K_s or event.key == pg.K_DOWN or event.key == pg.K_a or event.key == pg.K_LEFT or event.key == pg.K_d or event.key == pg.K_RIGHT:
                        self.player.set_move_dir(0, 0)

                    if event.key == pg.K_RSHIFT or event.key == pg.K_LSHIFT:
                        self.player.walk()

    def spawn_enemies(self, num):
        start = 0
        for i in range(num):
            enemy_x = random.randint(0, WIDTH - tile_size)
            start += 102
            enemy_y = start
            flip = random.choice(("h", "t"))
            speed = random.randint(8, 15)
            if flip == "t":
                speed *= -1
            enemy = Enemy(enemy_x, enemy_y, tile_size, tile_size, enemy_img, speed)
            self.enemies_list.append(enemy)
            if start > 760:
                start = 0

    def detect_Collisions(self, obj1, obj2):
        # check if colliding in the x dir
        if obj1.x > (obj2.x + obj2.width):
            return False
        elif (obj1.x + obj1.width) < obj2.x:
            return False

        # check if colliding in the x dir
        if obj1.y > (obj2.y + obj2.height):
            return False
        elif (obj1.y + obj1.height) < obj2.y:
            return False

        return True

    def show_start_screen(self):
        self.game_window.blit(self.background_img.image, (self.background_img.x, self.background_img.y))
        self.game_window.blit(self.treasure_img.image, (self.treasure_img.x, self.treasure_img.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        enemy = Enemy(WIDTH / 2, HEIGHT / 2, tile_size, tile_size, enemy_img, 0)
        self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        draw_Text(self.game_window, TITLE, 80, HEIGHT / 2.5, WIDTH / 4, cyan)
        draw_Text(self.game_window, "Press Enter To Play", 40, HEIGHT / 2.5, WIDTH / 2, cyan)
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        return "end"

    def show_game_over_screen(self):
        self.game_window.fill(black)
        draw_Text(self.game_window, "Game Over", 80, HEIGHT / 2.5, WIDTH / 4, red)
        draw_Text(self.game_window, "Press Enter To Restart", 40, HEIGHT / 2.5, WIDTH / 2, purple)

        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        return "end"
            # button_inputs = self.xbox_controller.get_buttons()
            # a = button_inputs.get("CONT_A")
            # if a > 0:
            #     waiting = False
            # start = button_inputs.get("CONT_START")
            # if start > 0:
            #     return "end"

    def nextLevel(self):
        self.level += 1
        self.player.collected = False
        self.resetLevel()
        self.enemies_list = []
        self.spawn_enemies(self.level)
        self.hasDiamond = random.choice([True,True,False,False,False,False])
        if self.hasDiamond:
            self.oneup_x = random.randint(0+tile_size,WIDTH-tile_size)
            self.oneup_y = random.randint(0 + tile_size, HEIGHT - tile_size)
        else:
            self.oneup_x = 1000
            self.oneup_y = 0
        self.extralife.x = self.oneup_x
        self.extralife.y = self.oneup_y


    def resetLevel(self):
        self.treasure_img.reset()
        self.player.reset()

