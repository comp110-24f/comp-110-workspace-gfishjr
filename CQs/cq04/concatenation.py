"""Defines a function that concatenates two strings"""

__author__: str = "730756982"


def concat(first_string: str, second_string: str) -> str:
    """returns the two strings concatenated"""
    return first_string + second_string


if __name__ == "__main__":
    # doesn't run this part if the file is being imported
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(first_string=word1, second_string=word2))
