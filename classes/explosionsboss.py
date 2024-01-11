import random

import pygame


class ExplosionBoss(pygame.sprite.Sprite):

    def __init__(self, center, explosion2_images):
        super().__init__()
        self.explosion2_images = explosion2_images
        self.image = self.explosion2_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60
        self.explosion2_sounds = [
            pygame.mixer.Sound('sounds/FL_sounds/explosions/explosion2.wav')
        ]
        for sound in self.explosion2_sounds:
            sound.set_volume(0.3)
        self.explosion2_sound = random.choice(self.explosion2_sounds)
        self.sound_played = False

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion2_images):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion2_images[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                if not self.sound_played:
                    self.explosion2_sound.play()
                    self.sound_played = True
