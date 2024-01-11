import pygame
import random
import math

from .constants import WIDTH, HEIGHT


class Boss(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 6
        self.direction = random.choice([(-1, 0), (1, 0)])
        self.shoot_timer = 0
        self.shots_fired = 0

    def update(self, enemy_bullets_group, player):
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.01) * 3
        self.rect.y += math.sin(pygame.time.get_ticks() * 0.01) * 3
        if self.shots_fired < 20:
            dx, dy = self.direction
            self.rect.x += dx * self.speed
            self.rect.y = max(self.rect.y, 50)

            if self.rect.left < 5:
                self.rect.left = 5
                self.direction = (1, 0)
            elif self.rect.right > WIDTH - 5:
                self.rect.right = WIDTH - 5
                self.direction = (-1, 0)

            self.shoot_timer += 1
            if self.shoot_timer >= 60:
                bullet1 = Boss_Bullet(self.rect.centerx - 20, self.rect.bottom)
                bullet2 = Boss_Bullet(self.rect.centerx + 20, self.rect.bottom)
                bullet3 = Boss_Bullet(self.rect.centerx, self.rect.bottom)
                enemy_bullets_group.add(bullet1, bullet2, bullet3)
                self.shoot_timer = 0
                self.shots_fired += 1
        else:
            self.speed = 10
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            direction = pygame.math.Vector2(dx, dy).normalize()

            self.rect.x += direction.x * self.speed
            self.rect.y += direction.y * self.speed


class Boss_Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/TH_level/bullets/bulletboss.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 10
        self.speed = 10

    def update(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:
            self.kill()
