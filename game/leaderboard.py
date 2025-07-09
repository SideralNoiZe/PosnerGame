import os
import json
import pygame
from .utils import display_message, WHITE, BLACK

def load_leaderboard():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    leaderboard_file = os.path.join(BASE_DIR, "leaderboard.json")
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, 'r') as f:
            return json.load(f)
    return []

def save_leaderboard(leaderboard):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    leaderboard_file = os.path.join(BASE_DIR, "leaderboard.json")
    with open(leaderboard_file, 'w') as f:
        json.dump(leaderboard, f)

def update_leaderboard(name, rt, errors):
    penalty = 0.1
    adjusted = rt + errors * penalty
    leaderboard = load_leaderboard()
    leaderboard.append({'name': name, 'overall_rt': adjusted, 'errors': errors})
    leaderboard = sorted(leaderboard, key=lambda x: (x['overall_rt'], x['errors']))[:10]
    save_leaderboard(leaderboard)

def show_leaderboard(screen, screen_width, screen_height, name, sounds):
    font = pygame.font.SysFont("Courier", 50, bold=True)
    leaderboard = load_leaderboard()
    screen.fill(WHITE)
    display_message(screen, "Top 10 Leaderboard", (screen_width//2,50),70)
    x = screen_width//2 - 300
    y = 120
    spacing = 200

    for i, e in enumerate(leaderboard):
        color = (0,255,0) if e['name'] == name else BLACK
        yy = y + i*60
        screen.blit(font.render(str(i+1), True, color), (x,yy))
        screen.blit(font.render(e['name'], True, color), (x+spacing,yy))
        screen.blit(font.render(f"{e['overall_rt']:.3f}", True, color), (x+2*spacing,yy))
        screen.blit(font.render(str(e['errors']), True, color), (x+3*spacing,yy))

    if any(e['name']==name for e in leaderboard[:10]):
        sounds["top_10_sound"].play()
    else:
        sounds["not_top_10_sound"].play()

    display_message(screen, "Premi SPAZIO per uscire", (screen_width//2, screen_height-100))
    pygame.display.flip()
    _wait_for_space()
    pygame.quit()

def _wait_for_space():
    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    waiting = False
