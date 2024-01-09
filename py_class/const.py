import pygame

list_consts = []


class ReadConstants:
    try:
        with open('data/const.txt', "r") as file:
            for line in file:
                list_consts.append(line)
    except FileNotFoundError:
        print('Файл не найден')


class Constants:
    width = 0
    height = 0
    white = 0
    black = 0
    green = 0
    red = 0
    yellow = 0
    FPS = 60

    def __init__(self):
        self.set_width()
        self.set_height()
        self.set_white()
        self.set_black()
        self.set_green()
        self.set_red()
        self.set_yellow()

    # размеры экрана:
    def set_width(self):
        self.width = int(list_consts[0])

    def get_width(self):
        return self.width

    def set_height(self):
        self.height = int(list_consts[1])

    def get_height(self):
        return self.height

    # используемые цвета:
    def set_white(self):
        self.white = (255, 255, 255)

    def get_white(self):
        return self.white

    def set_black(self):
        self.black = (0, 0, 0)

    def get_black(self):
        return self.black

    def set_green(self):
        self.green = (0, 128, 0)

    def get_green(self):
        return self.green

    def set_red(self):
        self.red = (255, 0, 0)

    def get_red(self):
        return self.red

    def set_yellow(self):
        self.yellow = (255, 215, 0)

    def get_yellow(self):
        return self.yellow


# иные:
const = Constants()
SCREEN = pygame.display.set_mode((const.get_width(), const.get_height()))
BACKGROUND_MENU = pygame.image.load("images/background.jpg")
BACKGROUND_ABOUT_US = pygame.image.load("images/about_as.jpg")
BACKGROUND_LEVELS = pygame.image.load("images/level.jpg")
