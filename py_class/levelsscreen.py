import pygame

from py_class.backgrounds import GameBackgrounds
from py_class.buttons_in_menu import Button
from py_class.const import Constants
from py_class.font import font_for_menu, font_for_buttons


class LevelsScreen:
    screen = None

    def __init__(self, scr):
        self.screen = scr
        self.init_screen()

    def init_screen(self):
        backgrounds = GameBackgrounds()
        pygame.mixer.music.load("sounds/mucis_for_menu.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1)
        self.screen.blit(backgrounds.get_background_levels(), (0, 0))
        exit_text = font_for_menu(55).render("Выберите, какой уровень вы хотите пройти?", True, "White")
        exit_rect = exit_text.get_rect(center=(620, 75))
        self.screen.blit(exit_text, exit_rect)

    def run(self):
        print('Открыли экран выбора уровней')
        level1_button = self.create_level1_button()
        level2_button = self.create_level2_button()
        levels_return_button = self.create_levels_return_button()

        const = Constants()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for button in [level1_button, level2_button, levels_return_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    return const.get_close_game_name()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if level1_button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_level1_screen_name()
                    if level2_button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_level2_screen_name()
                    if levels_return_button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_main_screen_name()

            pygame.display.update()

    def create_level1_button(self):
        return Button(
            image=pygame.image.load("images/background for button in menu.png"),
            pos=(640, 250),
            text_input="Первый",
            font=font_for_buttons(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

    def create_level2_button(self):
        return Button(
            image=pygame.image.load("images/background for button in menu.png"),
            pos=(640, 400),
            text_input="Второй",
            font=font_for_buttons(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

    def create_levels_return_button(self):
        return Button(
            image=None,
            pos=(640, 600),
            text_input="В МЕНЮ",
            font=font_for_menu(75),
            base_color="Black",
            hovering_color="Green",
        )

    def get_screen_name(self):
        const = Constants()
        return const.get_levels_screen_name()
