"""Mutating functions."""

__author__: str = "730756982"


def manual_append(list: list[int], num: int) -> None:
    """Appends num to list"""
    list.append(num)


def double(list: list[int]) -> None:
    """Doubles every number in a list"""
    index: int = 0
    while index < len(list):
        list[index] = list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2 = list_1
double(list=list_2)
print(list_1)
print(list_2)
