import pygame


class GameBackgrounds:

    def get_background_menu(self):
        return pygame.image.load("images/background.jpg")

    def get_background_about_us(self):
        return pygame.image.load("images/about_as.jpg")

    def get_background_levels(self):
        return pygame.image.load("images/level.jpg")
