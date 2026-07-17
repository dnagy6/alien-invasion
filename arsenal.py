import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """A class to manage the bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the arsenal and create a group to store bullets."""

        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update the position of bullets and get rid of old bullets."""

        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Remove bullets that have disappeared off the top of the screen."""

        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all active bullets to the screeen."""

        for bullet in self.arsenal.sprites():
            bullet.draw_bullet()

    def fire_bullet(self):
        """Create a new bullet and add it to the arsenal."""
        
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False