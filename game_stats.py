class GameStats():
    """Track runtime stats and state conditions for Alien Invasion"""
    def __init__(self, ship_limit):
        """Initialize operational stats dynamically based on game settings."""
        
        self.ships_left = ship_limit 
