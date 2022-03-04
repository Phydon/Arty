import sys
import pygame as pg

from settings import *
from pen import *


class Main():

    def __init__(self):
        # general setup
        self.screen = pg.display.set_mode((settings["WIDTH"], settings["HEIGHT"]))
        pg.display.set_caption('Arty')
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, settings["font_size_1"])
        self.font_2 = pg.font.SysFont(None, settings["font_size_1"])
        self.font_3 = pg.font.SysFont(None, settings["font_size_1"])
        self.click = False

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu(self):
        run = True
        while run:

            self.screen.fill(settings["GREY"])
            self.draw_text("Main Menu", self.font, (254, 254, 254), self.screen, 35, settings["HEIGHT"] - (settings["HEIGHT"] - 35))

            mx, my = pg.mouse.get_pos() # get mouse position

            # generate buttons
            button1_x, button1_y = (50, settings["HEIGHT"] - (settings["HEIGHT"] - 150))
            button1 = pg.Rect(button1_x, button1_y, 200, 70)
            button2_x, button2_y = (50, settings["HEIGHT"] - (settings["HEIGHT"] - 250))
            button2 = pg.Rect(button2_x, button2_y, 200, 70)

            # check if button is clicked
            if button1.collidepoint((mx, my)):
                # if clicked -> call main function
                if self.click:
                    self.main()
            if button2.collidepoint((mx, my)):
                # if clicked -> call options function
                if self.click:
                    self.options()

            # draw buttons
            pg.draw.rect(self.screen, settings["PURPLE"], button1)
            pg.draw.rect(self.screen, settings["PURPLE"], button2)

            # draw button text
            self.draw_text("Start", self.font, settings["LIGHT_GREY"], self.screen, button1_x + 30, button1_y + 25)
            self.draw_text("Options", self.font, settings["LIGHT_GREY"], self.screen, button2_x + 30, button2_y + 25)

            # check for events (mouse / keyboard clicks)
            self.click = False
            for event in pg.event.get():
                # exit condition
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False
                        pg.quit()
                        sys.exit()
                # mouse click event
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # update the display
            pg.display.update()
            self.clock.tick(settings["FPS"])

    def main(self):

        self.screen.fill(settings["GREY"])
        pens = [Dot() for _ in range(settings["quantity"])]
        

        run = True
        while run:

            self.click = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    # return to main menu
                    if event.key == pg.K_ESCAPE:
                        run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            for pen in pens:
                pen.draw()
                pen.randomwalk()

            pg.display.update()
            self.clock.tick(settings["FPS"])

    def options(self):
        run = True
        while run:

            self.screen.fill(settings["GREY"])
            self.draw_text("Options", self.font, (254, 254, 254), self.screen, 20, 20)

            self.click = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    # return to main menu
                    if event.key == pg.K_ESCAPE:
                        run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pg.display.update()
            self.clock.tick(settings["FPS"])


if __name__ == "__main__":
    pg.init()
    main = Main()
    main.main_menu()
