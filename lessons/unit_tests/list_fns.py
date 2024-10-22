"""Testing different functions."""

__author__: str = "730756982"


def get_first(input: list[str]) -> str:
    "Returns the first element in a list"
    return input[0]


def remove_first(input: list[str]) -> None:
    """Pop the first element off of the input list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Returns and removes the first element of the list"""
    first: str = input[0]
    input.pop(0)
    return first
