import pygame


class ConstantsReader:
    list_consts = []

    def __init__(self):
        try:
            with open('data\const.txt', "r") as file:
                for line in file:
                    self.list_consts.append(line)
        except FileNotFoundError:
            self.set_default_values()
            print('Файл const.txt не найден')

    def set_default_values(self):
        self.list_consts.append('1200')
        self.list_consts.append('800')

    def read_width(self) -> int:
        return int(self.list_consts[0])

    def read_height(self) -> int:
        return int(self.list_consts[1])


class Constants:
    width = 0
    height = 0
    white = 0
    black = 0
    green = 0
    red = 0
    yellow = 0
    FPS = 60

    main_screen_name = 'main'
    levels_screen_name = 'levels'
    study_screen_name = 'study'
    last_screen_name = 'last_screen'
    close_game = 'close_game'
    level1_screen = 'level1'
    level2_screen = 'level2'
    about_us_screen = 'about_us'

    def __init__(self):
        self.const_reader = ConstantsReader()
        self.set_width()
        self.set_height()
        self.set_white()
        self.set_black()
        self.set_green()
        self.set_red()
        self.set_yellow()

    # размеры экрана:
    def set_width(self):
        self.width = self.const_reader.read_width()

    def get_width(self):
        return self.width

    def set_height(self):
        self.height = self.const_reader.read_height()

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

    def get_main_screen_name(self):
        return self.main_screen_name

    def get_levels_screen_name(self):
        return self.levels_screen_name

    def get_study_screen_name(self):
        return self.study_screen_name

    def get_close_game_name(self):
        return self.close_game

    def get_last_screen_name(self):
        return self.last_screen_name

    def get_level1_screen_name(self):
        return self.level1_screen

    def get_level2_screen_name(self):
        return self.level2_screen

    def get_about_us_screen_name(self):
        return self.about_us_screen

