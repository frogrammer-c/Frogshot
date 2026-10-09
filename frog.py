import pygame

class Frog():
    def __init__(self, x: float, y: float, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color: str = "green"
        self.tongue_target: tuple[int] | None = None

    def handle_input(self, mouse_pos: tuple[int], buttons_pressed: tuple[bool]):
        if buttons_pressed[0]:
            self.tongue_target = mouse_pos
        else:
            self.tongue_target = None
            
    def update(self, dt: float, platforms: list):
        if self.tongue_target is not None:
            for platform in platforms:
                if platform.rect.clipline((self.x + self.width // 2, self.y + self.height // 2), self.tongue_target):
                    print("HI")

    def render(self, screen):
        if self.tongue_target is not None:
            frog_center = (self.x + self.width // 2, self.y + self.height // 2)
            pygame.draw.line(screen, "red", frog_center, self.tongue_target, 3)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
