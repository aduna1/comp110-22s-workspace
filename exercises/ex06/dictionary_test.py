"""Unit tests on dictonary functions."""

__author__ = "730469821"


from dictionary import invert, favorite_color, count

import pytest


def test_invert_empty_dict() -> None:
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_duplicate_key() -> None:
    test_dict: dict[str, str] = {"Adun": "Akinola", "Daniel": "Akinola", "Chris": "Odondi"}
    with pytest.raises(KeyError):
        invert(test_dict)


def test_invert() -> None:
    test_dict: dict[str, str] = {"apple": "fruit", "guitar": "instrument", "eagle": "bird"}
    assert invert(test_dict) == {"fruit": "apple", "instrument": "guitar", "bird": "eagle"}


def test_favorite_color_empty_dict() -> None:
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""
 

def test_favorite_color_tie() -> None:
    test_dict: dict[str, str] = {"Anna": "blue", "Adun": "yellow", "Ama": "yellow", "Gabby": "lavender", "Christiana": "lavender"}
    assert favorite_color(test_dict) == "yellow"


def test_favorite_color() -> None:
    test_dict: dict[str, str] = {"Mike": "red", "Isaac": "red", "Bill": "red", "Habin": "blue", "Flo": "green", "Gabby": "blue", "Elona": "blue", "Michelle": "beige", "Nerrissa": "brown"}
    assert favorite_color(test_dict) == "red"


def test_count_empty_list() -> None:
    test_list: list = []
    assert count(test_list) == {}


def test_count_short_list() -> None: 
    test_list: list[str] = ['happy']
    assert count(test_list) == {'happy': 1}


def test_count_repeat_item() -> None:
    test_list: list[str] = ['why', 'why', 'why', 'why', 'why']
    assert count(test_list) == {'why': 5}