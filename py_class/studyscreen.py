import random

import pygame

from classes.bullets import Bullet
from classes.constants import FPS, SHOOT_DELAY
from classes.enemies import Enemy1
from classes.explosions import Explosion
from classes.meteors import Meteors
from classes.player import Player
from py_class.buttons_in_menu import Button
from py_class.const import Constants
from py_class.controls import move_player
from py_class.font import font_for_menu
from py_class.functions import show_game_win


class StudyScreen:
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

    def run(self):
        print('Запустили уровень обучения')
        pygame.display.set_caption('Уровень обучения')
        explosions = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        enemy1_group = pygame.sprite.Group()
        bullet_refill_group = pygame.sprite.Group()
        meteor2_group = pygame.sprite.Group()

        bg_y_shift = -self.const.get_height()
        background_img = pygame.image.load("images/FL_images/background/background.png").convert()
        background_top = background_img.copy()
        current_image = background_img

        after_kill_particles = [
            pygame.image.load(f"images/FL_images/explosion/explosion{i}.png") for i in range(8)
        ]

        enemies = [
            pygame.image.load("images/FL_images/enemy/enemy1.png").convert_alpha(),
            pygame.image.load("images/FL_images/enemy/enemy2.png").convert_alpha(),
            pygame.image.load("images/FL_images/enemy/enemy3.png").convert_alpha(),
        ]

        stone_images_group = [
            pygame.image.load("images/FL_images/meteors/stone_1.png").convert_alpha(),
            pygame.image.load("images/FL_images/meteors/stone_2.png").convert_alpha(),
            pygame.image.load("images/FL_images/meteors/stone_3.png").convert_alpha(),
            pygame.image.load("images/FL_images/meteors/stone_4.png").convert_alpha(),
        ]
        extra_score_img = pygame.image.load('images/FL_images/icon.png')

        player_position_first = (self.const.get_width() // 2, self.const.get_height() - 100)
        # Константы под этот уровень.
        score = 0
        hi_score = 0
        player = Player()
        player_life = 100
        bullet_counter = 100

        # флаги.
        flag_to_paused_the_game = False
        flag_for_running_game = True

        # флаги для механики стрельбы.
        now_is_shot = False
        last_time_when_was_shot = 0

        while flag_for_running_game:

            if player_life < 50:
                player_life = 100
            if bullet_counter < 50:
                bullet_counter = 100

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.const.get_close_game_name()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not flag_to_paused_the_game:
                        if (
                                bullet_counter > 0
                                and pygame.time.get_ticks() - last_time_when_was_shot > SHOOT_DELAY
                        ):
                            last_time_when_was_shot = pygame.time.get_ticks()
                            bullet = Bullet(player.rect.centerx, player.rect.top)
                            bullets.add(bullet)
                            bullet_counter -= 1
                        now_is_shot = True

                    elif event.key == pygame.K_ESCAPE:
                        return self.const.get_about_us_screen_name()
                    elif event.key == pygame.K_p or event.key == pygame.K_PAUSE:
                        flag_to_paused_the_game = not flag_to_paused_the_game
                    elif not flag_to_paused_the_game:
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
                        now_is_shot = False
                    elif not flag_to_paused_the_game:
                        if event.key == pygame.K_LEFT:
                            player.stop_left()
                        elif event.key == pygame.K_RIGHT:
                            player.stop_right()
                        elif event.key == pygame.K_UP:
                            player.stop_up()
                        elif event.key == pygame.K_DOWN:
                            player.stop_down()
            if (
                    pygame.time.get_ticks() - last_time_when_was_shot > SHOOT_DELAY
                    and now_is_shot
                    and not flag_to_paused_the_game
            ):
                if bullet_counter > 0:
                    last_time_when_was_shot = pygame.time.get_ticks()
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)
                    bullet_counter -= 1

            if flag_to_paused_the_game:
                font = pygame.font.SysFont("Comic Sans MS", 40)
                text = font.render("PAUSE", True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.const.get_width() / 2, self.const.get_height() / 2))
                self.screen.blit(text, text_rect)
                pygame.display.flip()
                continue

            keys = pygame.key.get_pressed()

            if not flag_to_paused_the_game:
                move_player(keys, player)

                self.screen.blit(current_image, (0, bg_y_shift))
                background_top_rect = background_top.get_rect(topleft=(0, bg_y_shift))
                background_top_rect.top = bg_y_shift + self.const.get_height()
                self.screen.blit(background_top, background_top_rect)

            bg_y_shift += 1
            if bg_y_shift >= 0:
                bg_y_shift = -self.const.get_height()

            self.screen.blit(current_image, (0, bg_y_shift))
            background_top_rect = background_top.get_rect(topleft=(0, bg_y_shift))
            background_top_rect.top = bg_y_shift + self.const.get_height()
            self.screen.blit(background_top, background_top_rect)

            if score > hi_score:
                hi_score = score

            if random.randint(0, 120) == 0:
                enemy_img = random.choice(enemies)
                enemy_object = Enemy1(
                    random.randint(100, self.const.get_width() - 50),
                    random.randint(-self.const.get_height(), -50),
                    enemy_img,
                )
                enemy1_group.add(enemy_object)

            if random.randint(0, 90) == 0:
                meteor2_img = random.choice(stone_images_group)
                meteor2_object = Meteors(
                    random.randint(100, self.const.get_width() - 50),
                    random.randint(-self.const.get_height(), -50 - meteor2_img.get_rect().height),
                    meteor2_img,
                )
                meteor2_group.add(meteor2_object)

            if score >= 1000:
                show_game_win(score, "Поздравляем, Вы успешно прошли обучение")
                player.rect.topleft = player_position_first
                bullets.empty()
                bullet_refill_group.empty()
                meteor2_group.empty()
                enemy1_group.empty()
                explosions.empty()
                return self.const.get_about_us_screen_name()

            for bullet_refill in bullet_refill_group:

                bullet_refill.update()
                bullet_refill.draw(self.screen)

                if player.rect.colliderect(bullet_refill.rect):
                    if bullet_counter < 200:
                        bullet_counter += 50
                        if bullet_counter > 200:
                            bullet_counter = 200
                        bullet_refill.kill()
                    else:
                        bullet_refill.kill()

            for meteor2_object in meteor2_group:
                meteor2_object.update()
                meteor2_object.draw(self.screen)

                if meteor2_object.rect.colliderect(player.rect):
                    player_life -= 10
                    explosion = Explosion(meteor2_object.rect.center, after_kill_particles)
                    explosions.add(explosion)
                    meteor2_object.kill()
                    score += 20

                bullet_collisions = pygame.sprite.spritecollide(
                    meteor2_object, bullets, True
                )
                for bullet_collision in bullet_collisions:
                    explosion = Explosion(meteor2_object.rect.center, after_kill_particles)
                    explosions.add(explosion)
                    meteor2_object.kill()
                    score += 40

            for enemy_object in enemy1_group:
                enemy_object.update(enemy1_group)
                enemy1_group.draw(self.screen)

                if enemy_object.rect.colliderect(player.rect):
                    player_life -= 10
                    explosion = Explosion(enemy_object.rect.center, after_kill_particles)
                    explosions.add(explosion)
                    enemy_object.kill()
                    score += 20

                bullet_collisions = pygame.sprite.spritecollide(enemy_object, bullets, True)
                for bullet_collision in bullet_collisions:
                    explosion = Explosion(enemy_object.rect.center, after_kill_particles)
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

            player_life_bar = pygame.Surface(
                (player_life_bar_width, 30), pygame.SRCALPHA, 32
            )
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
            bullet_counter_bar = pygame.Surface(
                ((bullet_counter / 200) * 200, 30), pygame.SRCALPHA, 32
            )
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

            hi_score_surface = pygame.font.SysFont("Comic Sans MS", 20).render(
                f"Для прохождения обучения, наберите: 1000 очков.", True, (255, 255, 255)
            )
            hi_score_surface.set_alpha(128)
            hi_score_x_pos = (self.screen.get_width() - hi_score_surface.get_width()) // 2
            hi_score_y_pos = 0
            self.screen.blit(hi_score_surface, (hi_score_x_pos, hi_score_y_pos))

            hi_score_surface2 = pygame.font.SysFont("Comic Sans MS", 20).render(
                f"Здоровье и патроны автоматически пополняются.", True, (255, 255, 255)
            )
            hi_score_surface2.set_alpha(128)
            hi_score_x_pos2 = (self.screen.get_width() - hi_score_surface2.get_width()) // 2
            hi_score_y_pos2 = 30
            self.screen.blit(hi_score_surface2, (hi_score_x_pos2, hi_score_y_pos2))

            pygame.display.flip()

            self.clock.tick(FPS)

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
        return const.get_study_screen_name()
