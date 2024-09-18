"""Finds the number of instances of a character in a phrase"""

__author__: str = "730756982"


def num_instance(phrase: str, search_char: str) -> int:
    """This function returns the number of times that search_char appears in phrase"""
    count: int = 0
    index: int = 0
    # This while loop iterates through phrase, checking to see if
    # each character is equal to search_char.
    # If the character is equal to search_char, couunt will increase by one.
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
