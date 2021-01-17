import pygame
from pygame.locals import MOUSEMOTION

from troll import Troll

class GameScene():
    def __init__(self):
        self.background_color = pygame.Color('gray57')

        self.troll = Troll()

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.troll.handle_event(event)

    def render(self, screen):
        screen.fill(self.background_color)
        self.troll.render(screen)

        pygame.display.flip()

    def update(self):
        self.troll.update()