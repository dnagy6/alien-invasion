from pathlib import Path
import pathlib

class Settings:
    def __init__(self):
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width = 40
        self.ship_height = 60
        self.ship_speed = 5