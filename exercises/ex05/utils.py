"""An assignment on list related functions."""

__author__ = "730469821"


def only_evens(a: list[int]) -> list:
    """A function that returns only even numbers in a list of integers."""
    evens: list[int] = list()
    for item in a:
        if item % 2 == 0:
            evens.append(item)
    return evens


def sub(a_list: list[int], a: int, b: int) -> list:
    """A function that takes a list of integers and two indices and returns the items in the list between the two additional integer inputs."""
    sub_list: list[int] = list()
    if a < 0:
        a = 0
    if b > len(a_list):
        b = len(a_list) - 1 
    if len(a_list) == 0 or a > len(a_list) or b <= 0:
        return sub_list
    i: int = a
    while i < b:
        sub_list.append(a_list[i])
        i += 1
    return sub_list


def concat(a: list[int], b: list[int]) -> list:
    """A function that takes two lists and joins them together."""
    new_list: list[int] = a
    i: int = 0
    while i < len(b):
        new_list.append(b[i])
        i += 1
    return new_list
