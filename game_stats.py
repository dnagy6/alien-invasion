# from pathlib import Path
import json

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion



class GameStats():
    """Track runtime statistics, high scores, active level, and state conditions for Alien Invasion."""

    def __init__(self, game: "AlienInvasion"):
        """Initialize operational stats dynamically based on game settings and load saved scores."""
        
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Load persistent high score form JSON file or create initial record if absent."""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)

        else:
            self.hi_score = 0
            self.save_scores()
            # save the file

    def save_scores(self):
        """Write current all-time high score state out to the JSON save file."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e.value}')

    def reset_stats(self):
        """Reset dynamic statistics (lives left, score, level) for a fresh game session."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1


    def update(self, collisions):
        """Update active player score and evaluate high score benchmarks upon alien collisions."""
        # update score
        self._update_score(collisions)

        # update max_score
        self._update_max_score()

        # update high score
        self._update_hi_score()

    def _update_max_score(self):
        """Update single-session maximum score if current score surpasses it."""
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max: {self.max_score}')

    def _update_hi_score(self):
            """Update persistent high score if current score exceeds previous all-time record."""
            if self.score > self.hi_score:
                self.hi_score = self.score
            # print(f'Max: {self.max_score}')

    def _update_score(self, collisions):
        """Calculate and add point increments for all destroyed alien targets."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        print(f'Basic: {self.score}')
        

    def update_level(self):
        """Increment current game level counter upon clearing a fleet."""
        self.level += 1