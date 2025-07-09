import pygame

def show_instructions(screen, instructions1_path, instructions2_path, screen_width, screen_height):
    bg1 = pygame.image.load(instructions1_path)
    bg1 = pygame.transform.scale(bg1, (screen_width, screen_height))
    bg2 = pygame.image.load(instructions2_path)
    bg2 = pygame.transform.scale(bg2, (screen_width, screen_height))

    _wait_for_space(screen, bg1)
    _wait_for_space(screen, bg2)

def _wait_for_space(screen, background):
    screen.blit(background, (0, 0))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
