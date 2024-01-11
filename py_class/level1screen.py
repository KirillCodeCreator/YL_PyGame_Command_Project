import random

import pygame

from classes.bullets import Bullet
from classes.constants import FPS, SHOOT_DELAY
from classes.enemies import Enemy1
from classes.explosions import Explosion
from classes.player import Player
from py_class.const import Constants
from py_class.controls import move_player
from py_class.functions import show_game_over, show_game_win


class Level1Screen:
    screen = None

    def __init__(self, scr):
        self.screen = scr
        self.const = Constants()
        self.clock = pygame.time.Clock()
        self.surface = pygame.Surface((self.const.get_width(), self.const.get_height()))
        self.init_screen()

    def play_music_background(self):
        pygame.mixer.music.load('sounds/FL_sounds/background_music.mp3')
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(loops=-1)

    def init_screen(self):
        self.play_music_background()
        pygame.display.set_caption('Первый уровень')

    def run(self):
        print('Запустили экран уровня 1')
        explosions = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        enemy1_group = pygame.sprite.Group()
        extra_score_group = pygame.sprite.Group()
        black_hole_group = pygame.sprite.Group()

        bg_y_shift = -self.const.get_height()
        background_img2 = pygame.image.load('images/FL_images/background/background2.png').convert()
        background_top = background_img2.copy()
        current_image = background_img2

        explosion_images = [pygame.image.load(f"images/FL_images/explosion/explosion{i}.png") for i in range(8)]

        enemies_images = [
            pygame.image.load('images/FL_images/enemy/enemy1.png').convert_alpha(),
            pygame.image.load('images/FL_images/enemy/enemy2.png').convert_alpha(),
            pygame.image.load('images/FL_images/enemy/enemy3.png').convert_alpha()
        ]
        extra_score_img = pygame.image.load('images/FL_images/score/score_coin.png').convert_alpha()

        initial_player_pos = (self.const.get_width() // 2, self.const.get_height() - 100)

        score = 0
        hi_score = 0
        player = Player(5)
        player_life = 100
        bullet_counter = 100

        paused = False
        running = True

        is_shooting = False
        last_shot_time = 0

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not paused:
                        if bullet_counter > 0 and pygame.time.get_ticks() - last_shot_time > SHOOT_DELAY:
                            last_shot_time = pygame.time.get_ticks()
                            bullet = Bullet(player.rect.centerx, player.rect.top)
                            bullets.add(bullet)
                            bullet_counter -= 1
                        is_shooting = True

                    elif event.key == pygame.K_ESCAPE:
                        return self.const.get_levels_screen_name()
                    elif event.key == pygame.K_p or event.key == pygame.K_PAUSE:
                        paused = not paused
                    elif not paused:
                        if event.key == pygame.K_LEFT:
                            player.move_left()
                        elif event.key == pygame.K_RIGHT:
                            player.move_right()
                        elif event.key == pygame.K_UP:
                            player.move_up()
                        elif event.key == pygame.K_DOWN:
                            player.move_down()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE and player.original_image is not None:
                        player.image = player.original_image.copy()
                        is_shooting = False
                    elif not paused:
                        if event.key == pygame.K_LEFT:
                            player.stop_left()
                        elif event.key == pygame.K_RIGHT:
                            player.stop_right()
                        elif event.key == pygame.K_UP:
                            player.stop_up()
                        elif event.key == pygame.K_DOWN:
                            player.stop_down()

            if pygame.time.get_ticks() - last_shot_time > SHOOT_DELAY and is_shooting and not paused:
                if bullet_counter > 0:
                    last_shot_time = pygame.time.get_ticks()
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)
                    bullet_counter -= 1

            if paused:
                font = pygame.font.SysFont('Comic Sans MS', 40)
                text = font.render("PAUSE", True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.const.get_width() / 2, self.const.get_height() / 2))
                self.screen.blit(text, text_rect)
                pygame.display.flip()
                continue

            keys = pygame.key.get_pressed()

            if not paused:
                move_player(keys, player)

                self.screen.blit(current_image, (0, bg_y_shift))
                background_top_rect = background_top.get_rect(topleft=(0, bg_y_shift))
                background_top_rect.top = bg_y_shift + self.const.get_height()
                self.screen.blit(background_top, background_top_rect)

            bg_y_shift += 1
            if bg_y_shift >= 0:
                bg_y_shift = -self.const.get_height()

            if score == 0:
                current_image = background_img2
                background_top = background_img2.copy()

            self.screen.blit(current_image, (0, bg_y_shift))
            background_top_rect = background_top.get_rect(topleft=(0, bg_y_shift))
            background_top_rect.top = bg_y_shift + self.const.get_height()
            self.screen.blit(background_top, background_top_rect)

            if score > hi_score:
                hi_score = score

            if random.randint(0, 120) == 0:
                enemy_img = random.choice(enemies_images)
                enemy_object = Enemy1(
                    random.randint(100, self.const.get_width() - 50),
                    random.randint(-self.const.get_height(), -50),
                    enemy_img,
                )
                enemy1_group.add(enemy_object)

            if player_life <= 0:
                show_game_over(score)
                score = 0
                player_life = 100
                bullet_counter = 100
                player.rect.topleft = initial_player_pos
                bullets.empty()
                extra_score_group.empty()
                black_hole_group.empty()
                enemy1_group.empty()
                explosions.empty()
                return self.const.get_levels_screen_name()

            if score >= 500:
                show_game_win(score, "Поздравляем, Вы успешно прошли уровень 1", save=True)
                score = 0
                player_life = 100
                bullet_counter = 100
                player.rect.topleft = initial_player_pos
                bullets.empty()
                extra_score_group.empty()
                enemy1_group.empty()
                explosions.empty()
                return self.const.get_levels_screen_name()

            for extra_score in extra_score_group:
                extra_score.update()
                extra_score.draw(self.screen)

                if player.rect.colliderect(extra_score.rect):
                    score += 20
                    extra_score.kill()
                    extra_score.sound_effect.play()

            for enemy_object in enemy1_group:
                enemy_object.update(enemy1_group)
                enemy1_group.draw(self.screen)

                if enemy_object.rect.colliderect(player.rect):
                    player_life -= 10
                    explosion = Explosion(enemy_object.rect.center, explosion_images)
                    explosions.add(explosion)
                    enemy_object.kill()
                    score += 20

                bullet_collisions = pygame.sprite.spritecollide(enemy_object, bullets, True)
                for bullet_collision in bullet_collisions:
                    explosion = Explosion(enemy_object.rect.center, explosion_images)
                    explosions.add(explosion)
                    enemy_object.kill()
                    score += 50

            player_image_copy = player.image.copy()
            self.screen.blit(player_image_copy, player.rect)

            for explosion in explosions:
                explosion.update()
                self.screen.blit(explosion.image, explosion.rect)

            for bullet in bullets:
                bullet.update()
                self.screen.blit(bullet.image, bullet.rect)

                if bullet.rect.bottom < 0:
                    bullet.kill()
                    bullet_counter -= 1

            player_life_surface = pygame.Surface((200, 25), pygame.SRCALPHA, 32)
            player_life_surface.set_alpha(216)

            player_life_bar_width = int(player_life / 200 * 200)
            player_life_bar_width = max(0, min(player_life_bar_width, 200))

            player_life_bar = pygame.Surface((player_life_bar_width, 30), pygame.SRCALPHA, 32)
            player_life_bar.set_alpha(216)

            life_bar_image = pygame.image.load("images/FL_images/life_bar.png").convert_alpha()

            if player_life > 50:
                player_life_bar.fill((152, 251, 152))
            else:
                player_life_bar.fill((0, 0, 0))

            player_life_surface.blit(life_bar_image, (0, 0))
            player_life_surface.blit(player_life_bar, (35, 0))

            life_x_pos = 10
            self.screen.blit(player_life_surface, (life_x_pos, 10))

            bullet_counter_surface = pygame.Surface((200, 25), pygame.SRCALPHA, 32)
            bullet_counter_surface.set_alpha(216)
            bullet_counter_bar = pygame.Surface(((bullet_counter / 200) * 200, 30), pygame.SRCALPHA, 32)
            bullet_counter_bar.set_alpha(216)
            bullet_bar_image = pygame.image.load("images/FL_images/bullet_bar.png").convert_alpha()
            if bullet_counter > 50:
                bullet_counter_bar.fill((255, 23, 23))
            else:
                bullet_counter_bar.fill((0, 0, 0))
            bullet_counter_surface.blit(bullet_bar_image, (0, 0))
            bullet_counter_surface.blit(bullet_counter_bar, (35, 0))
            bullet_x_pos = 10
            bullet_y_pos = player_life_surface.get_height() + 20
            self.screen.blit(bullet_counter_surface, (bullet_x_pos, bullet_y_pos))

            score_surface = pygame.font.SysFont('Comic Sans MS', 30).render(f'{score}', True, (238, 232, 170))
            score_image_rect = score_surface.get_rect()
            score_image_rect.x, score_image_rect.y = self.const.get_width() - score_image_rect.width - extra_score_img.get_width() - 10, 10

            self.screen.blit(extra_score_img,
                             (score_image_rect.right + 5, score_image_rect.centery - extra_score_img.get_height() // 2))
            self.screen.blit(score_surface, score_image_rect)

            hi_score_surface = pygame.font.SysFont('Comic Sans MS', 20).render(
                f'Для прохождения данного уровня, наберите: 500 очков.', True, (255, 255, 255))
            hi_score_surface.set_alpha(128)
            hi_score_x_pos = (self.screen.get_width() - hi_score_surface.get_width()) // 2
            hi_score_y_pos = 0
            self.screen.blit(hi_score_surface, (hi_score_x_pos, hi_score_y_pos))

            pygame.display.flip()
            self.clock.tick(FPS)

    def get_screen_name(self):
        const = Constants()
        return const.get_level1_screen_name()
