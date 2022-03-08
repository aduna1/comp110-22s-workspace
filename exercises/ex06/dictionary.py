"""Practice with dictionary functions."""

__author__ = "730469821"


def invert(old_dictionary: dict[str, str]) -> dict[str, str]:
    invert_dict: dict[str, str] = {}
    for key in old_dictionary:
        value: str = old_dictionary[key]
        if value in invert_dict:
            raise KeyError("Duplicate Key.")
        invert_dict[value] = key
    return invert_dict


def favorite_color(name_color: dict[str, str]) -> str:
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
    d: dict[str, int] = {}
    for item in xs: 
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d