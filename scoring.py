import pygame

from config import window_size

class ScoreBoard():
    def __init__(self, scene):
        self.scene = scene
        self.font = pygame.font.Font(None, 30)
        self.color = pygame.Color('lightgoldenrod3')
        self.label = self.font.render('Total Klicks: ', True, self.color)
        field_width = 300
        self.position = ((window_size.width - field_width) // 2, 30)

    def render(self, screen):
        screen.blit(self.label, self.position)
        score = self.font.render(str(self.scene.score), True, self.color)
        screen.blit(score, (self.position[0] + self.label.get_width() + 5, self.position[1]))

    def update(self):
        pass