import pygame
from scene_manager import SceneManager

def main():
    pygame.init()
    manager = SceneManager()
    manager.loop()

if __name__ == "__main__":
    main()