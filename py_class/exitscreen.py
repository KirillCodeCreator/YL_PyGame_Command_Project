import pygame

from py_class.backgrounds import GameBackgrounds
from py_class.buttons_in_menu import Button
from py_class.const import Constants
from py_class.font import font_for_menu, font_for_buttons_text


class ExitScreen:
    screen = None

    def __init__(self, scr):
        self.screen = scr
        self.init_screen()

    def init_screen(self):
        backgrounds = GameBackgrounds()
        pygame.mixer.music.load("sounds/music_exit.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1)
        self.screen.fill(backgrounds.get_background_exit_game())
        exit_game_text = font_for_menu(45).render("Вы действительно хотите завершить игру?", True, "White")
        exit_game_rect = exit_game_text.get_rect(center=(640, 260))
        self.screen.blit(exit_game_text, exit_game_rect)

    def run(self):
        print('Открыли экран для подтверждения выхода из игры')
        yes_button = self.create_yes_button()
        no_button = self.create_no_button()
        const = Constants()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for button in [yes_button, no_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    return const.get_close_game_name()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_close_game_name()
                    if no_button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_main_screen_name()

            pygame.display.update()

    def create_yes_button(self):
        return Button(
            image=None,
            pos=(850, 460),
            text_input="Да",
            font=font_for_buttons_text(75),
            base_color="Yellow",
            hovering_color="Green",
        )

    def create_no_button(self):
        return Button(
            image=None,
            pos=(550, 460),
            text_input="Нет",
            font=font_for_buttons_text(75),
            base_color="Yellow",
            hovering_color="Green",
        )

    def get_screen_name(self):
        const = Constants()
        return const.get_last_screen_name()
