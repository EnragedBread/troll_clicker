import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from config import window_size, FPS
from title_scene import TitleScene

class SceneManager():
    def __init__(self):
        self.screen = pygame.display.set_mode(window_size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.switch_to(TitleScene())

    def switch_to(self, scene):
        self.scene = scene
        self.scene.manager = self

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.quit()
                self.scene.handle_event(event)

                self.scene.update()
                self.scene.render(self.screen)

                self.clock.tick(FPS)

    def quit(self):
        self.running = False