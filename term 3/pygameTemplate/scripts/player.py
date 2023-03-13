from scripts.settings import *


class Player(pg.sprite.Sprite):

    def __init__(self,game,x,y,img_dir,color_key):
        super(Player, self).__init__()

        self.image = self.get_img(img_dir)
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()
        self.game = game
        # self.image = pg.Surface((50,50))
        # self.image.fill(color)
        # self.rect = self.image.get_rect()

        self.rect.center = (x,y)
        self.moveX = 5
        self.moveY = 3
        self.leftclick = False

        self.addToGroups()

    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.player_group.add(self)

    def get_img(self,img_dir):
        self.img = pg.image.load(img_dir).convert()
        self.img = pg.transform.scale(self.img,(50,40))
        #self.player_img = pg.transform.flip(self.player_img,False,True)
        return self.img


    def update(self):
        # attach icon to mouse
        # mouse_pos = pg.mouse.get_pos()
        # mouse_x = mouse_pos[0]
        # mouse_y = mouse_pos[1]
        # self.rect.centerx = mouse_x
        # self.rect.centery = mouse_y
        self.rect.center = pg.mouse.get_pos()
        self.leftclick = pg.mouse.get_pressed()[0]

        # screen wrapping
        if not solid_bounds:
            if self.rect.left > WIDTH:
                self.rect.right = 0
            elif self.rect.right < 0:
                self.rect.left = WIDTH
            if self.rect.top > HEIGHT:
                self.rect.bottom = 0
            elif self.rect.bottom < 0:
                self.rect.top = HEIGHT

        else:
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
