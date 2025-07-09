import pygame
from game.assets import load_assets
from game.menu import main_menu
from game.instructions import show_instructions
from game.trials import posner_task, valid_reaction_times, invalid_reaction_times, error_count
from game.leaderboard import update_leaderboard, show_leaderboard
from game.utils import display_message

# Init
pygame.init()
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
assets = load_assets()

# Music
pygame.mixer.music.load(assets["music"])
pygame.mixer.music.play(-1)

# Main menu
if main_menu(screen, screen_width, screen_height, assets["title_image"]):
    # Name input
    from game.name_input import get_participant_name

    name = get_participant_name(screen, screen_width, screen_height)

    # Instructions
    show_instructions(screen, assets["instructions1"], assets["instructions2"], screen_width, screen_height)
    pygame.mixer.music.fadeout(2000)

    # Task
    posner_task(screen, screen_width, screen_height, name, assets)

    # Results
    avg_valid = sum(valid_reaction_times)/len(valid_reaction_times) if valid_reaction_times else 0
    avg_invalid = sum(invalid_reaction_times)/len(invalid_reaction_times) if invalid_reaction_times else 0
    total = len(valid_reaction_times)+len(invalid_reaction_times)
    avg_all = (sum(valid_reaction_times)+sum(invalid_reaction_times))/total if total else 0

    penalty = 0.1
    adjusted = avg_all + error_count*penalty
    validity = avg_invalid - avg_valid if valid_reaction_times and invalid_reaction_times else 0

    screen.fill((255,255,255))
    display_message(screen, "RISULTATI", (screen_width//2,100),100)
    y0 = screen_height//2 -150
    display_message(screen, f"RT (Overall): {avg_all:.3f}s", (screen_width//2 -200,y0), centered=False)
    display_message(screen, f"RT (Valid): {avg_valid:.3f}s", (screen_width//2 -200,y0+90), centered=False)
    display_message(screen, f"RT (Invalid): {avg_invalid:.3f}s", (screen_width//2 -200,y0+180), centered=False)
    display_message(screen, f"Validity Effect: {validity:.3f}s", (screen_width//2 -200,y0+270), centered=False)
    display_message(screen, f"Errors: {error_count}", (screen_width//2 -200,y0+360), centered=False)
    display_message(screen, "Premi SPAZIO per classifica", (screen_width//2, y0+500))
    pygame.display.flip()

    waiting=True
    while waiting:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()
                exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_SPACE:
                    waiting=False

    update_leaderboard(name, adjusted, error_count)
    show_leaderboard(screen, screen_width, screen_height, name, assets)
