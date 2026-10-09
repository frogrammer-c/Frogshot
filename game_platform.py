import pygame

class Platform():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, screen):
        pygame.draw.rect(screen, "chartreuse4", (self.x, self.y, self.width, self.height))