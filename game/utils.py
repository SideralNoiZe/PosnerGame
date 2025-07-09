import pygame
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def display_message(screen, text, position, font_size=70, color=BLACK, centered=True):
    font = pygame.font.Font(None, font_size)
    message = font.render(text, True, color)
    if centered:
        rect = message.get_rect(center=position)
    else:
        rect = message.get_rect(topleft=position)
    screen.blit(message, rect)

def countdown(screen, screen_width, screen_height, message, seconds):
    big_font = pygame.font.Font(None, int(screen_height * 200 / 1080))
    small_font = pygame.font.Font(None, int(screen_height * 100 / 1080))

    for i in range(seconds, 0, -1):
        screen.fill(WHITE)
        m = small_font.render(message, True, BLACK)
        screen.blit(m, m.get_rect(center=(screen_width // 2, screen_height // 2 - 100)))
        n = big_font.render(str(i), True, BLACK)
        screen.blit(n, n.get_rect(center=(screen_width // 2, screen_height // 2)))
        pygame.display.flip()
        time.sleep(1)
