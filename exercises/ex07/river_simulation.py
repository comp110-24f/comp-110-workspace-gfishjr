"""Brings everything together to simulate a river ecosystem."""

# imports river class
from exercises.ex07.river import River

__author__: str = "730756982"

"""Creates anew river starting with ten fish and two bears."""
my_river: River = River(num_fish=10, num_bears=2)

# Views the current river status.
my_river.view_river()
# Passes one week in the river.
my_river.one_river_week()
