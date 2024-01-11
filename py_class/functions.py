import pygame

from py_class.const import Constants
from py_class.scores import Scores

const = Constants()
screen = pygame.display.set_mode((const.get_width(), const.get_height()))


def music_background():
    pygame.mixer.music.load('sounds/FL_sounds/background_music.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loops=-1)


def show_game_over(score):
    scores = Scores()
    count = int(scores.get_scores_from_file())
    scores.save_to_file(score + count)
    constants = Constants()
    font = pygame.font.SysFont('Impact', 50)
    font_small = pygame.font.SysFont('Impact', 30)
    text = font.render("GAME OVER", True, (139, 0, 0))
    text_rect = text.get_rect(center=(constants.get_width() / 2, constants.get_height() / 2 - 50))
    score_text = font_small.render(f"Ваш накопленный рейтинг {score + count} очков", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(constants.get_width() / 2, constants.get_height() / 2 + 50))
    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.mixer.music.load('sounds/FL_sounds/gameover.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(3000)


def show_game_win(score, message, save: bool):
    if save == True:
        scores = Scores()
        count = int(scores.get_scores_from_file())
        scores.save_to_file(score + count)
    constants = Constants()
    font = pygame.font.SysFont('Impact', 50)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(constants.get_width() / 2, constants.get_height() / 2 - 50))
    screen.blit(text, text_rect)
    if save == True:
        font2 = pygame.font.SysFont('Impact', 35)
        text2 = font2.render(f"Ваш накопленный рейтинг {score + count} очков", True, (255, 255, 200))
        text2_rect = text.get_rect(center=(constants.get_width() / 2 + 200, constants.get_height() / 2 + 25))
        screen.blit(text2, text2_rect)
    pygame.display.flip()
    pygame.mixer.music.load('sounds/FL_sounds/win.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(3000)
