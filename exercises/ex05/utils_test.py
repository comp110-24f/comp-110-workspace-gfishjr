import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""Tests the list utility functions"""

__author__: str = "730756982"


def test_only_evens() -> None:
    """Tests use case of only_evens function if there are even and odd numbers"""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]


def test_only_evens2() -> None:
    """Tests use case of only_evens function if there are even and odd numbers"""
    assert only_evens([2, 2, 3, 2, 2, 7, 4]) == [2, 2, 2, 2, 4]


def test_only_evens3() -> None:
    """Tests use case of only_evens function if there are no even numbers"""
    assert only_evens([5, 7, 9, 3, 3]) == []


def test_only_evens4() -> None:
    """Tests edge case of only_evens when the input list is empty"""
    assert only_evens([]) == []


def test_sub() -> None:
    """Tests use case of only_evens function"""
    assert sub([4, 7, 2, 9, 4, 3], 1, 4) == [7, 2, 9]


def test_sub2() -> None:
    """Tests use case of only_evens function"""
    assert sub([3, 5, 8, 6, 9, 2, 5], 0, 5) == [3, 5, 8, 6, 9]


def test_sub3() -> None:
    """Tests edge case when first is less than 0 and last
    is more than the length of the list"""
    assert sub([1, 3, 5], -4, 8) == [1, 3, 5]


def test_sub4() -> None:
    """Tests edge case when first is more than the length of the list"""
    assert sub([4, 6, 8], 5, 8) == []


def test_sub5() -> None:
    """Tests edge case when last is 0"""
    assert sub([7, 8, 9, 5, 4], -4, 0) == []


def test_sub6() -> None:
    """Tests edge case when input list is empty"""
    assert sub([], 4, 6) == []


def test_add_at_index() -> None:
    """Tests use case of add_at_index function when number is inserted into
    middle of list"""
    num_list: list[int] = [1, 9, 4, 7]
    add_at_index(num_list, 5, 2)
    assert num_list == [1, 9, 5, 4, 7]


def test_add_at_index2() -> None:
    """Tests use case of add_at_index when number is added at end of list"""
    num_list: list[int] = [5, 1, 4]
    add_at_index(num_list, 6, 3)
    assert num_list == [5, 1, 4, 6]


def test_add_at_index3() -> None:
    """Tests use case of add_at_index when number is added to start of list"""
    num_list: list[int] = [1, 5]
    add_at_index(num_list, 4, 0)
    assert num_list == [4, 1, 5]


def test_add_at_index_indexerror() -> None:
    """Tests to make sure the function raises an index error for an invalid index"""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 4, 6)
