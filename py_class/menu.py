import sys

import pygame

from py_class.buttons_in_menu import Button
from py_class.font import font_for_menu, font_for_buttons_text
from py_class.font import font_for_buttons
from py_class.const import SCREEN
from py_class.const import BACKGROUND_MENU
from py_class.const import BACKGROUND_ABOUT_US
from py_class.const import BACKGROUND_LEVELS

pygame.init()
pygame.display.set_caption("К ЗВЁЗДАМ!")


def choice_level():
    flag = True
    while flag:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BACKGROUND_LEVELS, (0, 0))

        EXIT_TEXT = font_for_menu(55).render(
            "Выберите, какой уровень вы хотите пройти?", True, "White"
        )
        EXIT_RECT = EXIT_TEXT.get_rect(center=(640, 75))
        SCREEN.blit(EXIT_TEXT, EXIT_RECT)

        LEVEL_1_BUTTON = Button(
            image=pygame.image.load("images/background for button in menu.png"),
            pos=(640, 250),
            text_input="Первый",
            font=font_for_buttons(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        LEVEL_2_BUTTON = Button(
            image=pygame.image.load("images/background for button in menu.png"),
            pos=(640, 400),
            text_input="Второй",
            font=font_for_buttons(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        LEVEL_BACK = Button(
            image=None,
            pos=(640, 600),
            text_input="В МЕНЮ",
            font=font_for_menu(75),
            base_color="Black",
            hovering_color="Green",
        )

        for button in [LEVEL_1_BUTTON, LEVEL_2_BUTTON, LEVEL_BACK]:
            button.changeColor(LEVEL_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_1_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    main_menu()
                if LEVEL_2_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    main_menu()
                if LEVEL_BACK.checkForInput(LEVEL_MOUSE_POS):
                    main_menu()
        pygame.display.update()


def about_us():
    flag = True
    pygame.mixer.music.load("sounds/music_about_us.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1)
    while flag:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BACKGROUND_ABOUT_US, (0, 0))

        OPTIONS_TEXT = font_for_menu(65).render("Информация", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_PLAY = Button(
            image=None,
            pos=(640, 600),
            text_input="пробовать",
            font=font_for_menu(75),
            base_color="Black",
            hovering_color="Green",
        )

        OPTIONS_PLAY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PLAY.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_PLAY.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def exit_function():
    flag = True
    pygame.mixer.music.load("sounds/music_exit.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1)
    while flag:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        EXIT_TEXT = font_for_menu(45).render(
            "Вы точно хотите покинуть игру?", True, "White"
        )
        EXIT_RECT = EXIT_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(EXIT_TEXT, EXIT_RECT)

        EXIT_YES = Button(
            image=None,
            pos=(850, 460),
            text_input="Да",
            font=font_for_buttons_text(75),
            base_color="Yellow",
            hovering_color="Green",
        )

        EXIT_YES.changeColor(OPTIONS_MOUSE_POS)
        EXIT_YES.update(SCREEN)

        EXIT_NO = Button(
            image=None,
            pos=(550, 460),
            text_input="Нет",
            font=font_for_buttons_text(75),
            base_color="Yellow",
            hovering_color="Green",
        )

        EXIT_NO.changeColor(OPTIONS_MOUSE_POS)
        EXIT_NO.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_YES.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if EXIT_NO.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    flag = True
    pygame.mixer.music.load("sounds/mucis_for_menu.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1)
    while flag:
        SCREEN.blit(BACKGROUND_MENU, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font_for_menu(100).render("К ЗВЁЗДАМ!", True, "#002137")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(
            image=pygame.image.load("images/background for button in menu.png"),
            pos=(640, 250),
            text_input="Уровни",
            font=font_for_buttons(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("images/background for button in menu.png"),
            pos=(640, 400),
            text_input="Учение",
            font=font_for_buttons(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load("images/background for button in menu.png"),
            pos=(640, 550),
            text_input="Уйти",
            font=font_for_buttons(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.stop()
                    choice_level()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.stop()
                    about_us()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    exit_function()

        pygame.display.update()
        programIcon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(programIcon)
