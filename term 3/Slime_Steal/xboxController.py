import pygame as pg


class Controller():
    def __init__(self, cont_number=0):
        self.dead_zone = .04
        try:
            self.controller = pg.joystick.Joystick(cont_number)
            self.controller.init()
            try:
                cont_id = self.controller.get_id()
            except AttributeError:
                cont_id = self.controller.get_id()
        except IOError:
            print("no controller connected")

    def get_hat(self):
        hat = self.controller.get_hat(0)
        x = hat[0]
        y = hat[1] * -1
        # dictionary (stores key value pairs)
        hat_dict = {"H_X": x, "H_Y": y}
        return hat_dict

    def get_buttons(self):
        a = self.controller.get_button(0)
        b = self.controller.get_button(1)
        x = self.controller.get_button(2)
        y = self.controller.get_button(3)
        L_joyb = self.controller.get_button(4)
        R_joyb = self.controller.get_button(5)


        buttons_dict = {"CONT_A": a, "CONT_X": x, "CONT_B": b, "CONT_Y": y, "LJOYB": L_joyb, "RJOYB": R_joyb, }
        return buttons_dict

    def get_axes(self):
        left_y = self.controller.get_axis(0)
        left_x = self.controller.get_axis(1)
        right_y = self.controller.get_axis(2)
        right_x = self.controller.get_axis(3)
        left_trig = self.controller.get_axis(4)
        right_trig = self.controller.get_axis(5)

        if left_x > -self.dead_zone and left_x < self.dead_zone:
            left_x = 0
        if left_y > -self.dead_zone and left_y < self.dead_zone:
            left_y = 0
        if right_x > -self.dead_zone and right_x < self.dead_zone:
            right_x = 0
        if right_y > -self.dead_zone and right_y < self.dead_zone:
            right_y = 0

        axis_dict = {"LJOY_Y": left_y, "LJOY_X": left_x, "RJOY_Y": right_y, "RJOY_X": right_x, "LTRIG": left_trig,
                     "RTRIG": right_trig, }
        return axis_dict