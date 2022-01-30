"""Practice with if-then-else statements."""

__author__ = "730469821"

choice: int = int(input("Enter a number: "))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice > 75:
        print("C")
    else:
        print("D")