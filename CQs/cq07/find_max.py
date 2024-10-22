"""Creates a function that returns the max int in a list
and removes all instances of max in the list"""

__author__: str = "730756982"


def find_and_remove_max(input: list[int]) -> int:
    """Returns the max int in the list and removes all instances of it"""
    # returns negative one if the list is empty
    if len(input) == 0:
        return -1
    # finds the max int in the list
    max: int = input[0]
    for num in input:
        # if the number is bigger than the max, sets the max to that number
        if num > max:
            max = num
    # removes all instances of max in the list
    index: int = 0
    while index < len(input):
        if input[index] == max:
            # removes the number at that index if it is the max number
            input.pop(index)
            # if a number is being removed, decreases the index by one
            index -= 1
        index += 1
    return max
