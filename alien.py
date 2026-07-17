import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        
        """Initialize the alien and set its starting position."""
        
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right,left, and down, depending on the fleet direction."""
        
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.y += self.settings.fleet_drop_speed
        
        self.x += temp_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Return if alien is at edge of screen."""
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left
        )
        

    def draw_alien(self):
        """Draw the alien at its current location."""

        self.screen.blit(self.image, self.rect)