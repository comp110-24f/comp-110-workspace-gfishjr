from CQs.cq07.find_max import find_and_remove_max

"""Tests the find_and_remove_max function"""

__author__: str = "730756982"


def test_find_and_remove_max() -> None:
    """Use case - returns expected value"""
    assert find_and_remove_max([5, 6, 3, 1, 5, 7]) == 7


def test_find_and_remove_max2() -> None:
    """Use casee - mutates list in the expected way"""
    a: list[int] = [8, 2, 4, 8, 3, 8, 8]
    find_and_remove_max(a)
    assert a == [2, 4, 3]


def test_find_and_remove_max3() -> None:
    """Edge case - returns correct value with unconventional output"""
    assert find_and_remove_max([]) == -1
