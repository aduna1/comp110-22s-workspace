"""Testing the functionality of list related functions."""

__author__ = "730469821"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests only_evens function for empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_all_odd() -> None:
    """Tests only_evens function for a list of odd integers."""
    test_list: list[int] = [3, 9, 23, 99]
    assert only_evens(test_list) == []


def test_only_evens_negative() -> None:
    """Tests only_evens function for a list including negative integers."""
    test_list: list[int] = [-24, -25, 18, -144]
    assert only_evens(test_list) == [-24, 18, -144]


def test_sub_empty() -> None:
    """Tests sub function for a an empty list."""
    test_list: list[int] = []
    ts: int = 0
    te: int = 0
    assert sub(test_list, ts, te) == []


def test_sub_start_negative() -> None:
    """Tests sub function for a starting index that is less than zero."""
    test_list: list[int] = [19, 13, 28, 45, 68, 70]
    ts: int = -4
    te: int = 3
    assert sub(test_list, ts, te) == [19, 13, 28]


def test_sub_short() -> None:
    """Tests sub function for a short list."""
    test_list: list[int] = [1, 2, 3]
    ts: int = 0
    te: int = 1
    assert sub(test_list, ts, te) == [1]


def test_concat_one_empty() -> None:
    """Tests concat function for one empty list of two list inputs."""
    test_a: list[int] = [1, 2, 3, 4]
    test_b: list[int] = []
    assert concat(test_a, test_b) == [1, 2, 3, 4]


def test_concat_single_item_lists() -> None:
    """Tests concat function for single item list inputs."""
    test_a: list[int] = [1]
    test_b: list[int] = [5]
    assert concat(test_a, test_b) == [1, 5]


def test_concat_multiple_items() -> None:
    """Tests concat function for two list inputs with multiple items."""
    test_a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_b: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert concat(test_a, test_b) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
