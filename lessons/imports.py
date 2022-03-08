"""Examples of importing in Python."""


from lessons import helpers

#  Alias as a module / imported name
from lessons import helpers as hp

#  Import names defined globally in a module
from lessons.helpers import THE_ANSWER, powerful


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}.")
    print(powerful(2, 4))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()