"""Defines a function that prints the formatted pairs of each character in the
two input strings"""

__author__: str = "730756982"


def get_coords(xs: str, ys: str) -> None:
    # this function prints the coordinate pairs of two strings
    index_one: int = 0
    index_two: int = 0
    while index_one < len(xs):
        # iterates through each value in the first string
        while index_two < len(ys):
            # iterates through each value in the second string
            print("(" + xs[index_one] + "," + ys[index_two] + ")")
            index_two += 1
        index_one += 1
        # resets the second index so it starts at the beginning of the string
        index_two = 0
