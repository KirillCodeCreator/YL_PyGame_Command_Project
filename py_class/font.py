import pygame


def font_for_menu(size):
    try:
        # попытка загрузить шрифт
        return pygame.font.Font("fonts/menu_font.otf", size)
    except pygame.error:
        # обработка ошибки, если шрифт не найден
        print('Ошибка: Шрифт не найден.')
        return None


def font_for_buttons(size):
    try:
        # попытка загрузить шрифт
        return pygame.font.Font("fonts/button_font.ttf", size)
    except FileNotFoundError:
        # обработка ошибки, если шрифт не найден
        print('Ошибка: Шрифт не найден.')
        return None


def font_for_buttons_text(size):
    try:
        # попытка загрузить шрифт
        return pygame.font.Font("fonts/exit_button_font.otf", size)
    except FileNotFoundError:
        # обработка ошибки, если шрифт не найден
        print('Ошибка: Шрифт не найден.')
        return None
