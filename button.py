import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    """A UI class for creating interaction, clickable buttons with centered text labels."""
    def __init__(self, game: 'AlienInvasion', msg):
        """Initialize button dimensions, font settings, position rect, and prep rendered message."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_width, self.settings.button_height)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Render text string into an image surface and center its bounding box within button rect."""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw (self):
        """Blit colored button background rectangle and overlaid message surface to the screen."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Check if target mouse coordinates fall within button's clickable bounding rect."""
        return self.rect.collidepoint(mouse_pos)

