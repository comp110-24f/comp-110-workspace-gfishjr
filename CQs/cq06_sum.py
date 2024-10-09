"""Summing the elements of a list using different loops"""

__author__: str = "730756982"


def w_sum(vals: list[float]) -> float:
    """returns the sum of the elements in a list by
    looping through the list with a while loop"""
    sum: float = 0.0
    index: int = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """returns the sum of the elements in a list by
    looping through the list using the for/in loop"""
    sum: float = 0.0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """returns the sum of the elements in a list by
    looping through the list using the for/ in range loop"""
    sum: float = 0.0
    for num in range(len(vals)):
        sum += vals[num]
    return sum
