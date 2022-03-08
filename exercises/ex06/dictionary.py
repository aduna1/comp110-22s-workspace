"""Practice with dictionary functions."""

__author__ = "730469821"


def invert(old_dictionary: dict[str, str]) -> dict[str, str]:
    """A function that inverts a dictionary input, making the keys the values and vice versa."""
    invert_dict: dict[str, str] = {}
    for key in old_dictionary:
        value: str = old_dictionary[key]
        if value in invert_dict:
            raise KeyError("Duplicate Key.")
        invert_dict[value] = key
    return invert_dict


def favorite_color(name_color: dict[str, str]) -> str:
    """A function that returns the most frequently occurring color in a dictionary of names and favorite colors."""
    fav_colors: dict[str, int] = {}
    for key in name_color:
        value: str = name_color[key]
        if value in fav_colors:
            fav_colors[value] += 1
        else:
            fav_colors[value] = 1
    max: int = 0
    mode_color: str = ""
    for key in fav_colors:
        if fav_colors[key] > max:
            max = fav_colors[key]
            mode_color = key
    return mode_color


def count(xs: list[str]) -> dict[str, int]:
    """A function that counts the number of times a string appears in a list and constructs a dictionary that assigns the number of times a string appears to said string."""
    d: dict[str, int] = {}
    for item in xs: 
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d