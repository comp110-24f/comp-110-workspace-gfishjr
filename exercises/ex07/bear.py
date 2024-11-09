"""File to define Bear class."""

__author__: str = "730756982"


class Bear:
    """Bear class initialization and methods."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear with an age and hunger score of 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases age and hunger score by one each day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increases the bear's hunger score by the number of fish it has eaten."""
        self.hunger_score += num_fish
        return None
