from scripts.settings import *


class Player(pg.sprite.Sprite):

    def __init__(self,game,x,y,img,color):
        super(Player, self).__init__()
        self.game = game
        self.image = img
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width+.85/2)
        # for debugging
        if debugging:
            pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.center = (x,y)

        self.moveX = 0
        self.addToGroups()
        self.can_shoot = True
        self.ammo = 10



    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.player_group.add(self)

    # def get_img(self,img_dir):
    #     self.img = pg.image.load(img_dir).convert()
    #     self.img = pg.transform.scale(self.img,(50,50))
    #     #self.player_img = pg.transform.flip(self.player_img,False,True)
    #     return self.img

    def setMoveX(self,value):
        self.moveX = value
    def shoot(self):
        self.can_shoot = False
        Bullet(self.game,self.rect.centerx,self.rect.top-2,self.game.bullet_img)
    def update(self):
        self.moveX = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.setMoveX(-move_speed)
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.setMoveX(move_speed)
        if keystate[pg.K_SPACE]:
            if self.can_shoot and self.ammo > 0:
                self.shoot()
        if keystate[pg.K_SPACE] == False:
            self.can_shoot == True

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
            self.rect.x += self.moveX


class Bullet (pg.sprite.Sprite):
    def __init__(self,game,x,y):
        super(Bullet, self).__init__()
        self.game = game
        self.image = pg.Surface((5, 10))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.moveY = -10
        self.addToGroups()

    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.bullet_group.add(self)
    def update(self):
        self.rect.y += self.moveY
        if self.rect.bottom < 0:
            self.kill()


