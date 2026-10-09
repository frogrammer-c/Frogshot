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
        self.out_of_bounds = False

    def handle_input(self, mouse_pos: tuple[int], buttons_pressed: tuple[bool]):
        if buttons_pressed[0]:
            self.mouse_target = mouse_pos
        else:
            self.move = False
            self.tongue_target = None
            self.mouse_target = None
            
    def update(self, dt: float, platforms: list):
        self.move = False

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

        def move():
            if self.move:
                frog_center_x = self.x + self.width / 2
                frog_center_y = self.y + self.height / 2
                target_x, target_y = self.tongue_target
                direction_x = target_x - frog_center_x
                direction_y = target_y - frog_center_y
                distance = (direction_x ** 2 + direction_y ** 2) ** 0.5

                if distance > 0:
                    acceleration = 1200
                    self.velocity_x += direction_x / distance * acceleration * dt
                    self.velocity_y += direction_y / distance * acceleration * dt

                speed = (self.velocity_x ** 2 + self.velocity_y ** 2) ** 0.5
                max_speed = 600
                if speed > max_speed:
                    scale = max_speed / speed
                    self.velocity_x *= scale
                    self.velocity_y *= scale

                travel_x = self.velocity_x * dt
                travel_y = self.velocity_y * dt
                if distance <= (travel_x ** 2 + travel_y ** 2) ** 0.5:
                    self.x = target_x - self.width / 2
                    self.y = target_y - self.height / 2
                    self.velocity_x = 0
                    self.velocity_y = 0
                    return
            else:
                self.velocity_x *= max(0, 1 - 4 * dt)
                self.velocity_y += 900 * dt

            self.x += self.velocity_x * dt
            self.y += self.velocity_y * dt

        def check_out_of_bounds():
            if self.x < 0:
                self.out_of_bounds = True
            if self.x + self.width > pygame.display.get_surface().get_width():
                self.out_of_bounds = True
            if self.y < 0:
                self.out_of_bounds = True
            if self.y + self.height > pygame.display.get_surface().get_height():
                self.out_of_bounds = True

        tongue_target()
        move()
        self.rect.topleft = (round(self.x), round(self.y))
        check_out_of_bounds()

    def render(self, screen):
        if self.tongue_target is not None:
            frog_center = (self.x + self.width // 2, self.y + self.height // 2)
            pygame.draw.line(screen, "red", frog_center, self.tongue_target, 3)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
