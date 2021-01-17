import random

import pygame

from config import window_size

class Troll(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect(
            topleft = (
                (window_size.width - self.surf.get_width()) // 2,
                (window_size.height - self.surf.get_height()) // 2
            )
        )
        self.delta_x = 0
        self.delta_y = 0

    def handle_event(self, event):
        if self.rect.collidepoint(event.pos):
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

            #self.delta_x = new_x - self.rect.x
            #self.delta_y = new_y - self.rect.y

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
