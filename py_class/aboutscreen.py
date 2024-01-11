import pygame

from py_class.backgrounds import GameBackgrounds
from py_class.buttons_in_menu import Button
from py_class.const import Constants
from py_class.font import font_for_menu


class AboutUsScreen:
    screen = None

    def __init__(self, scr):
        self.screen = scr
        self.init_screen()

    def init_screen(self):
        backgrounds = GameBackgrounds()
        pygame.mixer.music.load("sounds/music_about_us.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1)
        self.screen.blit(backgrounds.get_background_about_us(), (0, 0))
        start_study_text = font_for_menu(65).render("Информация", True, "Black")
        start_study_rect = start_study_text.get_rect(center=(640, 200))
        self.screen.blit(start_study_text, start_study_rect)

        target_text = font_for_menu(30).render("Цель игры - управлять самолетом, набирая очки.",
                                               True, "White")
        target_rect = target_text.get_rect(center=(640, 300))
        self.screen.blit(target_text, target_rect)

        target2_text = font_for_menu(30).render("Следует сбивать или уворачиваться от помех",
                                                True, "White")
        target2_rect = target2_text.get_rect(center=(640, 350))
        self.screen.blit(target2_text, target2_rect)

        button1_text = font_for_menu(30).render("Стрелки на клавиатуре - двигают самолет в соответсвующем направлении",
                                                True, "White")
        button1_rect = button1_text.get_rect(center=(640, 400))
        self.screen.blit(button1_text, button1_rect)

        button2_text = font_for_menu(30).render("Кнопка Стрелять - выпустить снаряды для сбития помехи", True, "White")
        button2_rect = button2_text.get_rect(center=(640, 450))
        self.screen.blit(button2_text, button2_rect)

        button3_text = font_for_menu(30).render("Для завершения обучения набирайте требуемое количество очков", True,
                                                "White")
        button3_rect = button3_text.get_rect(center=(640, 500))
        self.screen.blit(button3_text, button3_rect)

    def run(self):
        print('Открыли экран о нас')
        start_study_button = self.create_start_study_button()
        return_button = self.create_return_button()
        const = Constants()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for button in [start_study_button, return_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    return const.get_close_game_name()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_study_button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_study_screen_name()
                    if return_button.checkForInput(mouse_pos):
                        pygame.mixer.music.stop()
                        return const.get_main_screen_name()

            pygame.display.update()

    def create_start_study_button(self):
        return Button(
            image=None,
            pos=(840, 600),
            text_input="ПОПРОБОВАТЬ",
            font=font_for_menu(75),
            base_color="Black",
            hovering_color="Green",
        )

    def create_return_button(self):
        return Button(
            image=None,
            pos=(340, 600),
            text_input="В МЕНЮ",
            font=font_for_menu(75),
            base_color="Black",
            hovering_color="Green",
        )

    def get_screen_name(self):
        const = Constants()
        return const.get_about_us_screen_name()
