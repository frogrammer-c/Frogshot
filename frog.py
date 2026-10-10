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
        self.move = False
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.y_direction = 1
        self.out_of_bounds = False

    def handle_input(self, mouse_pos: tuple[int], buttons_pressed: tuple[bool]):
        if buttons_pressed[0]:
            self.mouse_target = mouse_pos
        else:
            self.move = False
            self.tongue_target = None
            self.mouse_target = None
            
    def update(self, dt: float, platforms: list):
        def tongue_target():
            if self.mouse_target is None:
                return

            self.tongue_target = self.mouse_target

            for platform in platforms:
                intersection_points = platform.rect.clipline((self.x + self.width // 2, self.y + self.height // 2), (self.mouse_target))

                if len(intersection_points) > 0:
                    self.tongue_target = intersection_points[0]
                    self.move = True
                    break

        def check_out_of_bounds():
            if self.x < 0:
                self.out_of_bounds = True
            if self.x + self.width > pygame.display.get_surface().get_width():
                self.out_of_bounds = True
            if self.y < 0:
                self.out_of_bounds = True
            if self.y + self.height > pygame.display.get_surface().get_height():
                self.out_of_bounds = True

        def move():
            self.velocity_y += dt * 10
            self.y = self.y + self.velocity_y

            if self.y < 0:
                self.velocity_y = -self.velocity_y
            if self.y + self.height > pygame.display.get_surface().get_height():
                self.velocity_y = -self.velocity_y

            print(self.velocity_y)

        tongue_target()
        move()
        check_out_of_bounds()

    def render(self, screen):
        if self.tongue_target is not None:
            frog_center = (self.x + self.width // 2, self.y + self.height // 2)
            pygame.draw.line(screen, "red", frog_center, self.tongue_target, 3)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
