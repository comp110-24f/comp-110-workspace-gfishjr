"""List utility functions"""

__author__: str = "730756982"


def only_evens(input: list[int]) -> list[int]:
    """returns a list of only the even numbers in the input list"""
    even_list: list[int] = []
    for num in input:
        # checks to see if the number is even
        if num % 2 == 0:
            # if so, it gets added to the list of even numbers
            even_list.append(num)
    return even_list


def sub(input: list[int], first: int, last: int) -> list[int]:
    """generates a list that is a subset of the input list,
    between the specified start index and one less than the end index"""
    # adjusts the variable start to be 0 if it is less than one
    if first < 0:
        first = 0
    # adjusts the variable last to be the length of the length of input
    # if it is more than the length of input
    if last > len(input):
        last = len(input)
    # initializes sub_list as empty
    sub_list: list[int] = []
    # adds all values from input list between first and one less
    # than last to the sub_list
    while first < last:
        sub_list.append(input[first])
        first += 1
    return sub_list


def add_at_index(input: list[int], value: int, insert_index: int) -> None:
    """Inserts a value into a list at a specified index"""
    # raises an error if the index is out of range
    if insert_index > len(input) or insert_index < 0:
        raise IndexError("Index is out of bounds for the input list")
    second_half: list[int] = []
    while insert_index < len(input):
        # creates a new list with all the numbers after the value that
        # is being inserted into the list and removes all these numbers
        # from the original list
        second_half.append(input[insert_index])
        input.pop(insert_index)
    # adds the value to the original list, which only contains the numbers that
    # should go before the value
    input.append(value)
    # adds the rest of the numbers after value from the second half list
    for num in second_half:
        input.append(num)
