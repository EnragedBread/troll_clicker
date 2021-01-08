import pygame
from pygame.locals import KEYDOWN, K_SPACE

from game_scene import GameScene

class TitleScene():
    def __init__(self):
        self.manager = None     # This should be set by the scene manager

        self.font_large = pygame.font.Font(None, 85)
        self.font_small = pygame.font.Font(None, 25)
        self.title_text = self.font_large.render("Kool Clickerz", True, pygame.Color('lavenderblush2'))
        self.continue_text = self.font_small.render("Press [space] to become the Koolest Klicker!!1", True, pygame.Color('gold1'))
        self.background_color = pygame.Color('grey22')
        self.line_space = 5

    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_SPACE:
            self.manager.switch_to(GameScene())

    def render(self, screen):
        screen.fill(self.background_color)
        y_offset = 0
        for text in [self.title_text, self.continue_text]:
            x = (screen.get_width() - text.get_width()) // 2
            y = (screen.get_height() - text.get_height()) // 2 + y_offset
            screen.blit(text, (x,y))
            y_offset += text.get_height() + self.line_space

        pygame.display.flip()

    def update(self):
        pass