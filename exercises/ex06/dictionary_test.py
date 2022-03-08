"""Unit tests on dictonary functions."""

__author__ = "730469821"


from dictionary import invert, favorite_color, count

import pytest


def test_invert_empty_dict() -> None:
    """Tests the invert function in the instance of an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_duplicate_key() -> None:
    """Test for key error in instance of duplicate keys after dictionary inversion."""
    test_dict: dict[str, str] = {"Adun": "Akinola", "Daniel": "Akinola", "Chris": "Odondi"}
    with pytest.raises(KeyError):
        invert(test_dict)


def test_invert() -> None:
    """Tests the use of the invert function."""
    test_dict: dict[str, str] = {"apple": "fruit", "guitar": "instrument", "eagle": "bird"}
    assert invert(test_dict) == {"fruit": "apple", "instrument": "guitar", "bird": "eagle"}


def test_favorite_color_empty_dict() -> None:
    """Test the favorite_color function in the instance of an empty dictionary input."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""
 

def test_favorite_color_tie() -> None:
    """Tests the favorite_color function in the instance of a tie in color frequency."""
    test_dict: dict[str, str] = {"Anna": "blue", "Adun": "yellow", "Ama": "yellow", "Gabby": "lavender", "Christiana": "lavender"}
    assert favorite_color(test_dict) == "yellow"


def test_favorite_color() -> None:
    """Tests the use of the favorite_color function."""
    test_dict: dict[str, str] = {"Mike": "red", "Isaac": "red", "Bill": "red", "Habin": "blue", "Flo": "green", "Gabby": "blue", "Elona": "blue", "Michelle": "beige", "Nerrissa": "brown"}
    assert favorite_color(test_dict) == "red"


def test_count_empty_list() -> None:
    """Tests the count function in the instance of an empty list input."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_single_item() -> None: 
    """Tests the count function in the instance of a single-item list input."""
    test_list: list[str] = ['happy']
    assert count(test_list) == {'happy': 1}


def test_count_repeat_item() -> None:
    """Tests the count function in the instance of a list input of one repeating item."""
    test_list: list[str] = ['why', 'why', 'why', 'why', 'why']
    assert count(test_list) == {'why': 5}