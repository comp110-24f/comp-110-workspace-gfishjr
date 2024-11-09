"""File to define River class."""

# imports fish and bear class
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730756982"


# Defines river class and methods.
class River:
    """River class initialization and methods."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # Populate the river with fish and bears.
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals from their lists if they are too old."""
        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(Fish())
        self.fish = surviving_fish
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(Bear())
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int):
        """Removes amount fish from the list of fish."""
        removed_fish: int = 0
        while removed_fish < amount:
            # Removes the first fish in the list.
            self.fish.pop(0)
            removed_fish += 1

    def bears_eating(self):
        """Simulates bears eating fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                # Increases bear's hunger score.
                bear.eat(3)
                # Removes fish from the river.
                self.remove_fish(amount=3)
        return None

    def check_hunger(self):
        """Removes bears from the list if their hunger score is too low."""
        surviving_bear: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bear.append(bear)
        self.bears = surviving_bear
        return None

    def repopulate_fish(self):
        """Increases the number of fish by 4 for every pair of fish."""
        num_fish: int = len(self.fish)
        # Number of pairs of fish, even if odd number of fish.
        num_pairs: int = num_fish // 2
        num_offspring: int = num_pairs * 4
        i: int = 0
        while i < num_offspring:
            self.fish.append(Fish())
            i += 1
        return None

    def repopulate_bears(self):
        """Increases the number of bears by 1 for every pair of bears."""
        num_bears: int = len(self.bears)
        # Number of pairs of bears, even if odd number of bears.
        num_pairs: int = num_bears // 2
        i: int = 0
        while i < num_pairs:
            self.bears.append(Bear())
            i += 1
        return None

    def view_river(self):
        """Prints the day in the river, number of fish, and number of bears."""
        print("~~~ Day " + str(self.day) + ": ~~~")
        print("Fish population: " + str(len(self.fish)))
        print("Bear population: " + str(len(self.bears)))
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1.
        self.day += 1
        # Simulate one day for all Bears.
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish.
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating.
        self.bears_eating()
        # Remove hungry Bear's from River.
        self.check_hunger()
        # Remove old Fish and Bear's from River.
        self.check_ages()
        # Simulate Fish repopulation.
        self.repopulate_fish()
        # Simulate Bear repopulation.
        self.repopulate_bears()
        # Visualize River.
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times to simulate a week in the river."""
        days: int = 0
        days_in_week: int = 7
        while days < days_in_week:
            self.one_river_day()
            days += 1
        return None
