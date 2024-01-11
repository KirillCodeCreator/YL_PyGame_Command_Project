import pygame


def font_for_menu(size):
    try:
        return pygame.font.Font("fonts/menu_font.otf", size)
    except pygame.error:
        print('Шрифт не найден.')
        return None


def font_for_buttons(size):
    try:
        return pygame.font.Font("fonts/button_font.ttf", size)
    except FileNotFoundError:
        print('Шрифт не найден.')
        return None


def font_for_buttons_text(size):
    try:
        return pygame.font.Font("fonts/exit_button_font.otf", size)
    except FileNotFoundError:
        print('Шрифт не найден.')
        return None
