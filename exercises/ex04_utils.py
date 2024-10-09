"""This program writes the function for 4 commonly used methods for lists"""

__author__: str = "730756982"


def all(input: list[int], num: int) -> bool:
    """returns true if all elements in a list are
    equal to a number, returns false otherwise"""
    index: int = 0
    # returns false if the list is empty
    if len(input) == 0:
        return False
    # loops through the list and sees if each index is equal to num
    while index < len(input):
        if input[index] != num:
            # returns false if an element in the list is not equal to num
            return False
        index += 1
    # returns true if you have looped through the entire list and every
    # element has been equal
    return True


def max(input: list[int]) -> int:
    """returns the biggest number in a list by looping
    through the list and comparing the current index to the
    previous index"""
    # raises a value error if the list is empty
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    # sets the max int to the first number in the list
    index: int = 0
    max_int: int = input[index]
    # increments the index by 1 so you are starting the loop
    # by comparing the first number to the second
    index += 1
    while index < len(input):
        # if the number at an index is greater than what the max is,
        # the max becomes that number
        if input[index] > max_int:
            max_int = input[index]
        index += 1
    return max_int


def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """returns whether or not two lists are equal by making sure
    both lists are the same length, and then comparing each element
    of the lists at the same index"""
    # starts by checking if the list lengths are equal
    # if not, returns false
    if len(input_1) == len(input_2):
        index: int = 0
        # loops through one list, checking to see if each element
        # is equal to the element at the same index in the other list
        while index < len(input_1):
            # returns false if any element is not equal
            if input_1[index] != input_2[index]:
                return False
            index += 1
        # if you have looped through the entire list and all elements
        # are equal, returns true
        return True
    else:
        return False


def extend(input_1: list[int], input_2: list[int]) -> None:
    """Mutates the first list by appending each element of the
    second list to it"""
    index: int = 0
    while index < len(input_2):
        # appends an element at a certain index in the second list to end of the first
        input_1.append(input_2[index])
        index += 1
