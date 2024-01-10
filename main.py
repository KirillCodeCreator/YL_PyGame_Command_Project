import sys

import pygame

from py_class.const import Constants
from py_class.mainscreen import MainScreen, LevelsScreen, StudyScreen
from py_class.menu import main_menu


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption("К ЗВЁЗДАМ!")
    programIcon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(programIcon)

    const = Constants()
    SCREEN = pygame.display.set_mode((const.get_width(), const.get_height()))
    next_screen_name = const.get_main_screen_name()

    # запускаем цикл перехода по экранам
    while True:
        if next_screen_name == const.get_main_screen_name():
            #открываем стартовый экран
            screen_cursor = MainScreen(SCREEN)
            next_screen_name = screen_cursor.run()
            if next_screen_name == const.get_close_game_name():
                break
        elif next_screen_name == const.get_levels_screen_name():
            # открываем экран для выбора уровней
            screen_cursor = LevelsScreen(SCREEN)
            next_screen_name = screen_cursor.run()
            if next_screen_name == const.get_close_game_name():
                break
        elif next_screen_name == const.get_study_screen_name():
            # открываем экран для обучения
            screen_cursor = StudyScreen(SCREEN)
            next_screen_name = screen_cursor.run()
            if next_screen_name == const.get_close_game_name():
                break

    # завершаем и выходим:
    pygame.quit()
    sys.exit()

'''main_menu()'''
