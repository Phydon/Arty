import pygame as pg
import random

from settings import *


class Pen():

    def __init__(self, color=settings["WHITE"]):
        self.screen = pg.display.set_mode((settings["WIDTH"], settings["HEIGHT"]))
        # self.mx, self.my = pg.mouse.get_pos() # get mouse position
        # self.x = self.mx
        # self.y = self.my
        self.x = random.randint(10, settings["WIDTH"] - 10)
        self.y = random.randint(10, settings["HEIGHT"] - 10)
        self.entity = pg.Rect(self.x, self.y, 2, 2)
        self.color = settings["color_list_white"][random.randint(0, len(settings["color_list_white"]) - 1)]
        self.velocity = random.randint(1, settings["velocity"])


    def draw(self):
        pg.draw.rect(self.screen, self.color, self.entity)


    def randomwalk(self):
        num = random.randrange(4)

        # left
        if num == 0 and self.entity.x - self.velocity > 0:
            self.entity.x -= self.velocity

        # right
        elif num == 1 and self.entity.x + self.velocity < settings["WIDTH"]:
            self.entity.x += self.velocity

        # up
        elif num == 2 and self.entity.y - self.velocity > 0:
            self.entity.y -= self.velocity

        # down
        elif num == 3 and self.entity.y + self.velocity < settings["HEIGHT"]:
            self.entity.y += self.velocity

        else:
            pass

        return self.entity


class Dot(Pen):

    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    pass
