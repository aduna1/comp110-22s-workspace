"""Wordle: an addicting game!"""

__author__ = "730469821"


def contains_char(word: str, character: str) -> bool:
    """A method of finding single characters in words of any length."""
    assert len(character) == 1
    i: int = 0
    while i < len(word):
        if word[i] == character: 
            return True
        else:
            i += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess_word: str, secret_word: str) -> str:
    """A way to indicate if a collection of guessed characters is right with emoji color boxes."""
    assert len(guess_word) == len(secret_word)
    emoji: str = ""
    i = 0
    while i < len(secret_word):
        if guess_word[i] == secret_word[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[i]) is True:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1
    return emoji
    

def input_guess(guess_length: int) -> str:
    """A way to check for guesses of correct length."""
    guess: str = input(f"Enter a {guess_length} character word: ")
    while len(guess) != guess_length:
        guess = input(f"That wasn't {guess_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the progrm and main game loop."""
    turn: int = 1
    tries: int = 6
    secret: str = "codes"
    while turn <= tries:
        print(f"=== Turn {turn}/{tries} ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/{tries} turns!")
            exit()
        else:
            turn += 1 
    print(f"X/{tries} - Sorry, try again tomorrow!")
 
 
if __name__ == "__main__": 
    main()