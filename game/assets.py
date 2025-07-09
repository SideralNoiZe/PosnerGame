import os
import pygame

def load_assets():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")

    assets = {
        "music": os.path.join(ASSETS_DIR, "title_music.mp3"),
        "correct_sound": pygame.mixer.Sound(os.path.join(ASSETS_DIR, "correct.mp3")),
        "wrong_sound": pygame.mixer.Sound(os.path.join(ASSETS_DIR, "wrong.mp3")),
        "top_10_sound": pygame.mixer.Sound(os.path.join(ASSETS_DIR, "goodjob_sound.mp3")),
        "not_top_10_sound": pygame.mixer.Sound(os.path.join(ASSETS_DIR, "fail_sound.mp3")),
        "title_image": os.path.join(ASSETS_DIR, "title_screen.jpg"),
        "instructions1": os.path.join(ASSETS_DIR, "istruzioni1.jpg"),
        "instructions2": os.path.join(ASSETS_DIR, "istruzioni2.jpg")
    }

    return assets
