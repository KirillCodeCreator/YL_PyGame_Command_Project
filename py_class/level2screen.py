import random

import pygame

from classes.bosses import Boss
from classes.bullets import Bullet
from classes.constants import FPS, SHOOT_DELAY
from classes.explosions import Explosion
from classes.explosionsboss import ExplosionBoss
from classes.player import Player
from py_class.const import Constants
from py_class.controls import move_player
from py_class.functions import show_game_over, show_boss_game_win


class Level2Screen:
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
        pygame.display.set_caption('Второй уровень (Босс)')

    def run(self):
        print('Запустили экран уровня 2')
        explosions = pygame.sprite.Group()
        explosions2 = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        enemy1_group = pygame.sprite.Group()
        boss1_group = pygame.sprite.Group()

        boss1_bullets = pygame.sprite.Group()

        boss1_health = 150
        boss1_health_bar_rect = pygame.Rect(0, 0, 150, 5)
        boss1_spawned = False

        bg_y_shift = -self.const.get_height()
        background_img3 = pygame.image.load('images/FL_images/background/background3.png').convert()
        background_top = background_img3.copy()
        current_image = background_img3
        explosion_for_boss = [pygame.image.load(f"images/FL_images/explosion2/explosion{i}.png") for i in range(18)]
        boss = pygame.image.load('images/FL_images/boss/boss.png').convert_alpha()

        initial_player_pos = (self.const.get_width() // 2, self.const.get_height() - 100)

        score = 0
        hi_score = 0
        player = Player(10)
        player_life = 200
        bullet_counter = 200

        paused = False
        running = True

        is_shooting = False
        last_shot_time = 0

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.const.get_close_game_name()

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

            if score > 3000:
                bg_y_shift += 2

            self.screen.blit(current_image, (0, bg_y_shift))
            background_top_rect = background_top.get_rect(topleft=(0, bg_y_shift))
            background_top_rect.top = bg_y_shift + self.const.get_height()
            self.screen.blit(background_top, background_top_rect)

            if score > hi_score:
                hi_score = score

            if score == 0 and not boss1_spawned:
                boss = boss
                boss1_object = Boss(
                    random.randint(200, self.const.get_width() - 100),
                    random.randint(-self.const.get_height(), -100),
                    boss,
                )
                boss1_group.add(boss1_object)
                boss1_spawned = True

            if player_life <= 0:
                show_game_over(score)
                boss1_spawned = False
                boss1_health = 150
                score = 0
                player_life = 200
                bullet_counter = 200
                player.rect.topleft = initial_player_pos
                bullets.empty()
                enemy1_group.empty()
                boss1_group.empty()
                explosions.empty()
                explosions2.empty()
                return self.const.get_levels_screen_name()

            if boss1_health <= 0:
                show_boss_game_win(score)
                boss1_spawned = False
                boss1_health = 150
                score = 0
                player_life = 200
                bullet_counter = 200
                player.rect.topleft = initial_player_pos
                bullets.empty()
                enemy1_group.empty()
                boss1_group.empty()
                explosions.empty()
                explosions2.empty()
                return self.const.get_levels_screen_name()

            for boss1_object in boss1_group:
                boss1_object.update(boss1_bullets, player)
                boss1_group.draw(self.screen)
                boss1_bullets.update()
                boss1_bullets.draw(self.screen)

                if boss1_object.rect.colliderect(player.rect):
                    player_life -= 20
                    explosion = ExplosionBoss(boss1_object.rect.center, explosion_for_boss)
                    explosions2.add(explosion)

                bullet_collisions = pygame.sprite.spritecollide(boss1_object, bullets, True)
                for bullet_collision in bullet_collisions:
                    explosion2 = Explosion(boss1_object.rect.center, explosion_for_boss)
                    explosions2.add(explosion2)
                    boss1_health -= 5
                    if boss1_health <= 0:
                        boss1_object.kill()
                        score += 400

                for boss1_bullet in boss1_bullets:
                    if boss1_bullet.rect.colliderect(player.rect):
                        player_life -= 20
                        boss1_bullet.kill()

                if boss1_health <= 0:
                    explosion = ExplosionBoss(boss1_object.rect.center, explosion_for_boss)
                    explosions2.add(explosion)
                    boss1_object.kill()

            if boss1_group:
                boss1_object = boss1_group.sprites()[0]
                boss1_health_bar_rect.center = (boss1_object.rect.centerx, boss1_object.rect.top - 5)
                pygame.draw.rect(self.screen, (255, 0, 0), boss1_health_bar_rect)
                pygame.draw.rect(self.screen, (0, 255, 0), (
                    boss1_health_bar_rect.left, boss1_health_bar_rect.top, boss1_health, boss1_health_bar_rect.height))

            player_image_copy = player.image.copy()
            self.screen.blit(player_image_copy, player.rect)

            for explosion in explosions:
                explosion.update()
                self.screen.blit(explosion.image, explosion.rect)

            for explosion2 in explosions2:
                explosion2.update()
                self.screen.blit(explosion2.image, explosion2.rect)

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

            hi_score_surface = pygame.font.SysFont('Comic Sans MS', 20).render(
                f'НЕ ПРИБЛЕЖАЙТЕСЬ К БОССУ, ЭТО СМЕРТЕЛЬНО ОПАСНО!', True,
                (255, 255, 255))
            hi_score_surface.set_alpha(128)
            hi_score_x_pos = (self.screen.get_width() - hi_score_surface.get_width()) // 2
            hi_score_y_pos = 0
            self.screen.blit(hi_score_surface, (hi_score_x_pos, hi_score_y_pos))

            pygame.display.flip()

            self.clock.tick(FPS)

    def get_screen_name(self):
        const = Constants()
        return const.get_level2_screen_name()
