import pygame

from scoring import ScoreBoard
from troll import Troll

class GameScene():
    def __init__(self):
        self.background_color = pygame.Color('gray57')

        self.scoreboard = ScoreBoard(self)
        self.troll = Troll(self)
        self.score = 0

    def handle_event(self, event):
        self.troll.handle_event(event)

    def render(self, screen):
        screen.fill(self.background_color)
        self.troll.render(screen)
        self.scoreboard.render(screen)

        pygame.display.flip()

    def update(self):
        self.troll.update()