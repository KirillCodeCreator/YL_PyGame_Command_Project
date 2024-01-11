import sys

import pygame

from py_class.aboutscreen import AboutUsScreen
from py_class.const import Constants
from py_class.exitscreen import ExitScreen
from py_class.level1screen import Level1Screen
from py_class.level2screen import Level2Screen
from py_class.mainscreen import MainScreen, LevelsScreen
from py_class.studyscreen import StudyScreen


# в этом методе выбираем экран
def select_screen(screen, next_screen_name):
    if next_screen_name == const.get_levels_screen_name():  # открываем экран для выбора уровней
        return LevelsScreen(screen)
    elif next_screen_name == const.get_level1_screen_name():  # открываем экран уровня 1
        return Level1Screen(screen)
    elif next_screen_name == const.get_level2_screen_name():  # открываем экран уровня 2
        return Level2Screen(screen)
    elif next_screen_name == const.get_about_us_screen_name():  # открываем экран с информацией и обучения
        return AboutUsScreen(screen)
    elif next_screen_name == const.get_study_screen_name():  # запускаем обучение
        return StudyScreen(screen)
    elif next_screen_name == const.get_last_screen_name():  # открываем финальный экран с вопросом о выходе из игры
        return ExitScreen(screen)
    else:
        return MainScreen(screen)

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
        screen_cursor = select_screen(SCREEN, next_screen_name)
        next_screen_name = screen_cursor.run()  #запускаем цикл обработки внутри выбранного экрана
        if next_screen_name == const.get_close_game_name():
            break

    # завершаем и выходим:
    pygame.quit()
    sys.exit()
