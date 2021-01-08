import pygame

class GameScene():
    def __init__(self):
        self.background_color = pygame.Color('gray57')

    def handle_event(self, event):
        pass

    def render(self, screen):
        screen.fill(self.background_color)
        pygame.display.flip()

    def update(self):
        pass