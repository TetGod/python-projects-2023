import pygame as pg


BLACK = pg.Color("black")
WHITE = pg.Color("white")

class TextPrint(object):
    def __init__(self,fontsize):
        self.fontsize = fontsize
        self.x = ""
        self.y = ""
        self.line_height = ""
        self.font = pg.font.Font(None, fontsize)
        self.reset()

    def tprint(self,screen,text):
        textBitmap = self.font.render(text,True,BLACK)
        screen.blit(textBitmap,(self.x,self.y))
        self.y += self.line_height



    def reset(self):
        self.x = 15
        self.y = 15
        self.line_height = self.fontsize-5
    def indent(self):
        self.x += 10
    def unindent(self):
        self.x -= 10


pg.init()
screen = pg.display.set_mode((500,800))
pg.display.set_caption("X Box Controller Test")

running = True

clock = pg.time.Clock()
fps = 40
text = TextPrint(25)
pg.joystick.init()
controller_list = []

while running:

    # tick clock
    clock.tick(fps)

    # get inputs
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.JOYBUTTONDOWN:
            print("Button pressed")
        elif event.type == pg.JOYBUTTONUP:
            print("Button released")


    screen.fill(WHITE)
    text.reset()

    joystick_count = pg.joystick.get_count()
    text.tprint(screen,"number of joysticks {}".format(joystick_count))
    text.indent()

    for i in range(joystick_count):
        # controller set up
        controller = pg.joystick.Joystick(i)
        controller.init()

        try:
            cont_id = controller.get_instance_id()
        except AttributeError:
            cont_id = controller.get_id()
        text.tprint(screen,"Controller {}".format(cont_id))
        text.indent()

        cont_name = controller.get_name()
        text.tprint(screen,"controller name {}".format(cont_name))

        try:
            guid = controller.get_guid()
        except AttributeError:
            pass
        else:
            text.tprint(screen,"GUID {}".format(guid))

        # Joy sticks / triggers
        axes = controller.get_numaxes()
        text.tprint(screen,"number of axes {}".format(axes))
        text.indent()
        for i in range(axes):
            axis = controller.get_axis(i)
            text.tprint(screen,"Axis {0} value {1:>6.3f}".format(i,axis))
        text.unindent()

        # buttons
        buttons = controller.get_numbuttons()
        text.tprint(screen,"number of buttons: {}".format(buttons))
        text.indent()

        for i in range(buttons):
            button = controller.get_button(i)
            text.tprint(screen, "button {:>2} value: {}".format(i,button))
        text.unindent()

        #  D pad
        hats = controller.get_numhats()
        text.tprint(screen, "Number of hats: {}".format(hats))
        text.indent()

        for i in range(hats):
            hat = controller.get_hat(i)
            text.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        text.unindent()

        text.unindent()


    #print(len(controller_list))


    # update

    # draw
    pg.display.flip()

pg.quit()
quit()
