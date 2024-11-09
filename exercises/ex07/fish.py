"""File to define Fish class."""

__author__: str = "730756982"


class Fish:
    """Fish class initialization and methods."""

    age: int

    def __init__(self):
        """Initializes the fish's age to 0."""
        self.age = 0
        return None

    def one_day(self):
        """Increases age by one each day."""
        self.age += 1
        return None
