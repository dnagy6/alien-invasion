import pygame.font
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
    # from alien_invasion import AlienInvasion

class HUD:
    """
    Manage and render heads-up display elements including score, level, and remaining lives. """

    def __init__(self,game):
        """Initialize HUD attributes, font settings, layout padding, and pre-render initial UI surfaces."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self._update_level()


    def _setup_life_image(self):
        """Load and scale ship sprite image used to represent remaining player lives."""
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_width, self.settings.ship_height))
        self.life_rect = self.life_image.get_rect()


    def update_scores(self):
        """Trigger sequence to update rendered text images for max, current, and high scores."""
        self._update_max_score()
        self._update_scores()
        self._update_hi_score()

    def _update_scores(self):
        """Render current score string and position its bounding rect relative to max score."""
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        """Render single-session max score string and position it at top right layout margin."""
        max_score_str = f'Max-Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        """Render all-time high score string centered at screen top layout margin."""
        hi_score_str = f'High-Score: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.right = self.boundaries.right - self.padding
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def _update_level(self):
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _draw_lives(self):
        """Blit remaining ship life icons in top-left corner using calculated padding offsets."""
        current_x = self.padding
        current_y = self.padding

        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding
    
    def draw(self):
        """Draw all HUD score elements and remaining life icons onto the main screen surface."""
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()