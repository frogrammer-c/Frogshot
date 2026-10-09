import pygame

class Frog():
    def __init__(self, x: float, y: float, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color: str = "green"
        self.mouse_target = None
        self.tongue_target: tuple[int] | None = None

    def handle_input(self, mouse_pos: tuple[int], buttons_pressed: tuple[bool]):
        if buttons_pressed[0]:
            self.mouse_target = mouse_pos
        else:
            self.tongue_target = None
            self.mouse_target = None
            
    def update(self, dt: float, platforms: list):
        if self.mouse_target is None:
            self.tongue_target = None
            return

        frog_center = (
            self.x + self.width // 2,
            self.y + self.height // 2
        )

        # Default: tongue reaches the mouse
        self.tongue_target = self.mouse_target

        for platform in platforms:
            intersection = platform.rect.clipline(
                frog_center,
                self.mouse_target
            )

            if intersection:
                self.tongue_target = intersection[0]
                break

    def render(self, screen):
        if self.tongue_target is not None:
            frog_center = (self.x + self.width // 2, self.y + self.height // 2)
            pygame.draw.line(screen, "red", frog_center, self.tongue_target, 3)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
