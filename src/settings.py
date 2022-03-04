import pygame as pg


settings = {}

# screen
settings["WIDTH"] = 1280
settings["WIDTH_CENTER"] = settings["WIDTH"] // 2
settings["HEIGHT"] = 720
settings["HEIGHT_CENTER"] = settings["HEIGHT"] // 2

settings["FPS"] = 60

# colours
settings["WHITE"] = (254, 254, 254)
settings["BLACK"] = (0, 0, 0)
settings["BLUE"] = (0, 0, 255)
settings["DARKVIOLETT"] = (25, 0, 51)
settings["VIOLETT"] = (51, 0, 102)
settings["RED"] = (255, 0, 0)
settings["LIGHTRED"] = (255, 51, 51)
settings["GREEN"] = (0, 255, 0)
settings["DARKGREEN"] = (51, 102, 0)
settings["YELLOW"] = (255, 255, 0)
settings["ORANGE"] = (255, 165, 0)
settings["TURQUOISE"] = (64, 224, 208)
settings["PURPLE"] = (35, 0, 15)
settings["PURPLE2"] = (128, 0, 128)
settings["LIGHT_GREY"] = (200, 200, 200)
settings["GREY"] = pg.Color("grey12")
settings["GREY2"] = (50, 50, 50)

# color lists
settings["color_list"] = [settings["WHITE"],settings["BLUE"],settings["VIOLETT"],settings["RED"],settings["GREEN"],settings["YELLOW"],settings["ORANGE"],settings["TURQUOISE"]]

settings["color_list_red"] = [(255, 0, 0), (200, 0, 0), (150, 0, 0), (100, 0, 0)]
settings["color_list_blue"] = [(0, 0, 255), (0, 0, 200), (0, 0, 150), (0, 0, 100)]
settings["color_list_white"] = [(254, 254, 254), (200, 200, 200), (150, 150, 150), (100, 100, 100)]

# fonts
settings["font_size_1"] = 32
settings["font_size_2"] = 20
settings["font_size_3"] = 44

# entites
settings["velocity"] = 5
settings["quantity"] = 100


if __name__ == "__main__":
    pass
