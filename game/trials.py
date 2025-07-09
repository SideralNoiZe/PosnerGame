import pygame
import time
import random
from .utils import display_message, countdown

WHITE = (255,255,255)
BLACK = (0,0,0)

valid_reaction_times = []
invalid_reaction_times = []
error_count = 0

def posner_task(screen, screen_width, screen_height, name, sounds):
    global error_count
    countdown(screen, screen_width, screen_height, "L'allenamento inizia tra:",3)
    screen.fill(WHITE)
    display_message(screen, "Get Ready...", (screen_width//2, screen_height//2))
    pygame.display.flip()
    pygame.time.wait(1000)
    run_trials(screen, screen_width, screen_height, 5, sounds, practice=True)
    screen.fill(WHITE)
    display_message(screen, "Tutto chiaro? Premi SPAZIO per iniziare", (screen_width//2, screen_height//2))
    pygame.display.flip()
    _wait_for_space()
    countdown(screen, screen_width, screen_height, "Inizio tra:",3)
    screen.fill(WHITE)
    display_message(screen, "Starting now...", (screen_width//2, screen_height//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    run_trials(screen, screen_width, screen_height, 20, sounds)

def run_trials(screen, screen_width, screen_height, n_trials, sounds, practice=False):
    global error_count
    cue_time = 0.5
    soa_time = 0.01
    square_size = 100
    x_offset = 360
    y = screen_height//2 - square_size//2

    trials = ['valid']*int(n_trials*0.8) + ['invalid']*int(n_trials*0.2)
    random.shuffle(trials)

    for t in trials:
        screen.fill(WHITE)
        left_x = screen_width//2 - x_offset - square_size
        right_x = screen_width//2 + x_offset

        # Fixation
        pygame.draw.rect(screen, BLACK, (left_x,y,square_size,square_size),2)
        pygame.draw.rect(screen, BLACK, (right_x,y,square_size,square_size),2)
        display_message(screen, "+", (screen_width//2, screen_height//2))
        pygame.display.flip()
        pygame.time.wait(1000)

        cue = random.choice(['left','right'])
        target = cue if t=='valid' else ('left' if cue=='right' else 'right')

        # Cue
        screen.fill(WHITE)
        _draw_boxes(screen, left_x, right_x, y, square_size)
        _draw_arrow(screen, cue, screen_width, screen_height)
        pygame.display.flip()
        pygame.time.wait(int(cue_time*1000))

        # Blank
        screen.fill(WHITE)
        _draw_boxes(screen, left_x, right_x, y, square_size)
        pygame.display.flip()
        pygame.time.wait(int(soa_time*1000))
        pygame.event.clear()

        # Target
        screen.fill(WHITE)
        _draw_boxes(screen, left_x, right_x, y, square_size)
        cx = left_x + square_size//2 if target=='left' else right_x + square_size//2
        pygame.draw.circle(screen, BLACK, (cx, y + square_size//2),7)
        pygame.display.flip()

        start = time.time()
        reacted = False
        while not reacted:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN:
                    if (e.key == pygame.K_LEFT and target == 'left') or (e.key == pygame.K_RIGHT and target == 'right'):
                        sounds["correct_sound"].play()
                        rt = time.time() - start
                        if not practice:
                            if t == 'valid':
                                valid_reaction_times.append(rt)
                            else:
                                invalid_reaction_times.append(rt)
                        reacted = True
                    elif (e.key == pygame.K_LEFT and target == 'right') or (e.key == pygame.K_RIGHT and target == 'left'):
                        sounds["wrong_sound"].play()
                        if not practice:
                            error_count += 1
                        reacted = True

def _draw_boxes(screen, left_x, right_x, y, size):
    pygame.draw.rect(screen, BLACK, (left_x,y,size,size),2)
    pygame.draw.rect(screen, BLACK, (right_x,y,size,size),2)

def _draw_arrow(screen, direction, screen_width, screen_height):
    length = int(screen_width *30/1920)
    thickness = int(screen_width *8/1920)
    arrowhead = int(screen_width *20/1920)
    total = length + arrowhead
    start_x = screen_width//2 - total//2
    y = screen_height//2

    if direction == 'left':
        pygame.draw.rect(screen, BLACK, (start_x + arrowhead, y - thickness//2, length, thickness))
        pygame.draw.polygon(screen, BLACK, [
            (start_x,y),
            (start_x + arrowhead, y - arrowhead//2),
            (start_x + arrowhead, y + arrowhead//2)
        ])
    else:
        pygame.draw.rect(screen, BLACK, (start_x, y - thickness//2, length, thickness))
        pygame.draw.polygon(screen, BLACK, [
            (start_x + length + arrowhead, y),
            (start_x + length, y - arrowhead//2),
            (start_x + length, y + arrowhead//2)
        ])

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
