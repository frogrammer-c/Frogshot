import pygame
from frog import Frog

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogshot")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

# Game states
MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"

state = MENU

dt = 0

frog = Frog(0, SCREEN_HEIGHT // 2, 50, 50)


def draw_text(text, x, y):
    image = font.render(text, True, (255, 255, 255))
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)

def main_menu():
    screen.fill((35, 85, 65))
    draw_text("FROGSHOT", SCREEN_WIDTH // 2, 130)
    draw_text("Press ENTER to start", SCREEN_WIDTH // 2, 230)

def game_running():
    screen.fill((110, 190, 210))
    # draw_text("GAME RUNNING", SCREEN_WIDTH // 2, 150)
    # draw_text("Gameplay goes here", SCREEN_WIDTH // 2, 230)
    # draw_text("Press ESC to end the run", SCREEN_WIDTH // 2, 310)

    # handle inputs
    frog.handle_input(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

    # update game
    frog.update(dt)

    # render game
    frog.render(screen)


def game_over():
    screen.fill((65, 45, 55))
    draw_text("GAME OVER", SCREEN_WIDTH // 2, 150)
    draw_text("Press ENTER for menu", SCREEN_WIDTH // 2, 250)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == PLAYING:
                    state = GAME_OVER
                else:
                    running = False

            elif event.key == pygame.K_RETURN:
                if state == MENU:
                    state = PLAYING
                elif state == GAME_OVER:
                    state = MENU

    # Draw the current state
    if state == MENU:
        main_menu()
    elif state == PLAYING:
        game_running()
    elif state == GAME_OVER:
        game_over()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()