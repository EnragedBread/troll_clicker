import os
import random
import time

import pygame
from pygame.locals import MOUSEMOTION, KEYDOWN, K_RCTRL, MOUSEBUTTONDOWN, RLEACCEL

from config import window_size

class Troll(pygame.sprite.Sprite):
    def __init__(self, scene):
        super().__init__()
        here = os.path.dirname(os.path.abspath(__file__))
        sound = os.path.join(here, 'troll_movement.wav')
        self.move_sound = pygame.mixer.Sound(sound)
        image = os.path.join(here, 'troll.png')

        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        self.rect = self.surf.get_rect(
            topleft = (
                (window_size.width - self.surf.get_width()) // 2,
                (window_size.height - self.surf.get_height()) // 2
            )
        )
        self.delta_x = 0
        self.delta_y = 0
        self.freeze = False
        self.freeze_time = 0
        self.scene = scene

    def handle_event(self, event):
        if event.type == MOUSEMOTION and self.freeze == False:
            if self.rect.collidepoint(event.pos):
               self._runaway_troll()

        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.scene.score += 1

        if event.type == KEYDOWN and event.key == K_RCTRL and self.freeze == False:
            self.freeze_time = time.time()
            self.freeze = True

    def render(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.rect.move_ip(self.delta_x, self.delta_y)

        if self.rect.right >= window_size.width:
            self.rect.left = 0

        if self.rect.left < 0:
            self.rect.right = window_size.width

        if self.rect.bottom >= window_size.height:
            self.rect.top = 0

        if self.rect.top < 0:
            self.rect.bottom = window_size.height

        self.delta_x = 0
        self.delta_y = 0

        if self.freeze and (time.time() - self.freeze_time >= 2):
            self.freeze = False
            self._runaway_troll()

    def _runaway_troll(self):
        new_x = random.randint(0, window_size.width - self.surf.get_width())
        new_y = random.randint(0, window_size.height - self.surf.get_height())

        if new_x >= self.rect.x:
            self.delta_x = max(new_x - self.rect.x, self.rect.width)
        else:
            self.delta_x = min(new_x - self.rect.x, -self.rect.width)

        if new_y >= self.rect.y:
            self.delta_y = max(new_y - self.rect.y, self.rect.height)
        else:
            self.delta_y = min(new_y - self.rect.y, -self.rect.height)

        self.move_sound.play()
