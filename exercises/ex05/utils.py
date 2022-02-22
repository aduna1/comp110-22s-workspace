"""An assignment on list utility functions."""

__author__ = "730469821"


def only_evens(a: list[int]) -> list:
    evens: list[int] = list()
    for item in a:
        if item % 2 == 0:
            evens.append(item)
    return evens


def sub(a_list: list[int], a: int, b: int) -> list:
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
    new_list: list[int] = a
    i: int = 0
    while i < len(b):
        new_list.append(b[i])
        i += 1
    return new_list
