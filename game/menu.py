import pygame
import random

def main_menu(screen, screen_width, screen_height, title_image_path):
    background_image = pygame.image.load(title_image_path)
    image_width = int(screen_width * (1600 / 1920))
    image_height = int(screen_height * (800 / 1080))
    background_image = pygame.transform.scale(background_image, (image_width, image_height))

    bg_x = random.randint(0, screen_width - image_width)
    bg_y = random.randint(0, screen_height - image_height)
    bg_speed_x = int(screen_width * (2 / 1920))
    bg_speed_y = int(screen_height * (2 / 1080))

    clock = pygame.time.Clock()

    while True:
        bg_x += bg_speed_x
        bg_y += bg_speed_y
        if bg_x <= 0 or bg_x + image_width >= screen_width:
            bg_speed_x = -bg_speed_x
        if bg_y <= 0 or bg_y + image_height >= screen_height:
            bg_speed_y = -bg_speed_y

        screen.fill((255, 255, 255))
        screen.blit(background_image, (bg_x, bg_y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

        clock.tick(60)
