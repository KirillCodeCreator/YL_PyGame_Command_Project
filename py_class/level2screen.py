import pygame

from py_class.backgrounds import GameBackgrounds
from py_class.buttons_in_menu import Button
from py_class.const import Constants
from py_class.font import font_for_menu


class Level2Screen:
    screen = None

    def __init__(self, scr):
        self.screen = scr
        self.init_screen()

    def init_screen(self):
        pass
        backgrounds = GameBackgrounds()
        #pygame.mixer.music.load("sounds/music_")
        #pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1)
        self.screen.blit(backgrounds.get_background_menu(), (0, 0))
        level_text = font_for_menu(55).render("Запустить Уровень 2", True, "White")
        level_rect = level_text.get_rect(center=(640, 75))
        self.screen.blit(level_text, level_rect)

    def run(self):
        print('Запустили экран уровня 2')
        const = Constants()
        button = self.create_return_button()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            button.changeColor(mouse_pos)
            button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    return const.get_close_game_name()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_levels_screen_name()

            pygame.display.update()

    def create_return_button(self):
        return Button(
            image=None,
            pos=(600, 650),
            text_input="НАЗАД",
            font=font_for_menu(75),
            base_color="White",
            hovering_color="Green",
        )

    def get_screen_name(self):
        const = Constants()
        return const.get_level2_screen_name()
