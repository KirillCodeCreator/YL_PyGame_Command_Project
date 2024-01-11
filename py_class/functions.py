import pygame
from classes.constants import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def music_background():
    pygame.mixer.music.load('sounds/FL_sounds/background_music.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loops=-1)


def show_game_over(score):
    font = pygame.font.SysFont('Impact', 50)
    font_small = pygame.font.SysFont('Impact', 30)
    text = font.render("GAME OVER", True, (139, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    score_text = font_small.render(f"ИТОГ: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.mixer.music.load('sounds/FL_sounds/gameover.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(2500)


def show_game_win(score):
    font = pygame.font.SysFont('Impact', 50)
    text = font.render("ВЫ ПРОШЛИ ОБУЧЕНИЕ!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.mixer.music.load('sounds/FL_sounds/win.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(2500)