from scripts.settings import *
from scripts.player import *
from scripts.enemies import *
from scripts.explosions import *


class Game(object):

    def __init__(self):
        self.playing = True
        pg.init()
        pg.mixer.init() # if using replit comment this out and anything else that uses sound at all
        # set up game screen
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        #pg.display.set_icon()
        self.clock = pg.time.Clock()
        self.mod_img = []
        self.explosion_animation = {}
        self.explosion_animation["L"] = []
        self.explosion_animation["S"] = []

        self.load_imgs()

        # create sprite groups
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.bullet_group = pg.sprite.Group()


        # create player as a player object
        self.player = Player(self,WIDTH/2,HEIGHT - 50,self.player_img,BLACK)

        # create enemies
        for i in range(10):
            Mob(self,random.choice(self.mod_img),BLACK)



    def load_imgs(self):
        self.bg_img = pg.image.load(os.path.join(background_folder,bg_img)).convert()
        self.bg_img = pg.transform.scale(self.bg_img,(WIDTH,HEIGHT))
        self.player_img = pg.image.load(os.path.join(player_folder,player_img_location)).convert()
        self.player_img = pg.transform.scale(self.player_img,(player_w,player_h))
        for i in range(10):
            z = pg.image.load(os.path.join(enemy_folder,str.format("Meteor_0{}.png",i)))
            z = pg.transform.scale(z,(50,50))
            self.mod_img.append(z)
        self.bullet_img = pg.image.load(os.path.join(bullets_folder,bullet_img))
        self.bullet_img = pg.transform.scale(self.bullet_img,(bullet_w,bullet_h))

        for i in range(9):
            filename = str.format("",i)
            img = pg.image.load(os.path.join(explosion_folder,filename)).convert()
            img.set_colorkey(BLACK)
            img_l = pg.transform.scale(img,(75,75))
            img_s = pg.transform.scale(img, (25, 25))
            self.explosion_animation["L"].append(img_l)
            self.explosion_animation["S"].append(img_s)

    def gameLoop(self):
        while self.playing:
            # tick clock
            self.clock.tick(fps)
            # check events
            self.checkEvents()
            # update all
            self.update()
            # draw
            self.draw()

    def checkEvents(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.playing = False
            # movement
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_a or event.key == pg.K_LEFT:
            #         self.player.setMoveX(-move_speed)
            #     if event.key == pg.K_d or event.key == pg.K_RIGHT:
            #         self.player.setMoveX(move_speed)
            # if event.type == pg.KEYUP:
            #     if event.key == pg.K_a or event.key == pg.K_LEFT or event.key == pg.K_d or event.key == pg.K_RIGHT:
            #         self.player.moveX = 0


    def update(self):
        self.all_sprites.update()

        hits = pg.sprite.spritecollide(self.player,self.enemy_group,False,pg.sprite.collide_circle)
        if hits:
            # game over
            self.playing = False
        hits = pg.sprite.groupcollide(self.enemy_group,self.bullet_group,True,True)
        if hits:
            for hit in hits:
                Explosion(self,hit.rect.center, "S")


    def draw(self):
        self.screen.fill(DEFAULT_COLOR)
        self.screen.blit(self.bg_img,self.bg_img.get_rect())
        self.all_sprites.draw(self.screen)


        # must be the last line in draw section
        pg.display.flip()

    def startScreen(self):
        pass
    def endScreen(self):
        pass

