import pygame
import os
import json
from .utils import display_message, WHITE, BLACK

def get_participant_name(screen, screen_width, screen_height):
    input_box = pygame.Rect(screen_width//2 -150, screen_height//2, 300,50)
    name = ""
    active = True
    done = False
    big_font = pygame.font.Font(None,100)
    underscore_spacing = 100
    underscore_width = 80
    underscore_thickness = 5

    leaderboard = _load_leaderboard()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN and len(name)==3:
                        if any(e['name']==name for e in leaderboard):
                            display_message(screen, "Nome già presente", (screen_width//2,screen_height//2+100), 50, (255,0,0))
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            name=""
                        else:
                            done=True
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name)<3 and event.unicode.isalpha():
                        name += event.unicode.upper()

        screen.fill(WHITE)
        display_message(screen, "IL TUO NOME", (screen_width//2,screen_height//2-150),100)

        display_name = name + "_"*(3-len(name))
        for i, letter in enumerate(display_name):
            x = screen_width//2 - underscore_spacing + i*underscore_spacing
            y = screen_height//2

            line_start = (x-underscore_width//2, y+60)
            line_end = (x+underscore_width//2, y+60)
            pygame.draw.line(screen, BLACK, line_start, line_end, underscore_thickness)

            if letter != "_":
                letter_surface = big_font.render(letter, True, BLACK)
                screen.blit(letter_surface, letter_surface.get_rect(center=(x,y)))

        pygame.display.flip()

    return name

def _load_leaderboard():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    leaderboard_file = os.path.join(BASE_DIR, "leaderboard.json")
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, 'r') as f:
            return json.load(f)
    return []
