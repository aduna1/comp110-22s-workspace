"""Wordle: an addicting game!"""

__author__ = "730469821"


def contains_char(word: str, character: str) -> bool:  # this function makes it possible for the game to test the characters of the user's guess.
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


def emojified(guess_word: str, secret_word: str) -> str:  # this function displays different color emoji boxes based on the correctness of the guessed letters and their location.
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
    

def input_guess(guess_length: int) -> str:  # this function ensures that the user inputs a guess of the desired length, in wordle's case, 5!
    """A way to check for guesses of correct length."""
    guess: str = input(f"Enter a {guess_length} character word: ")
    while len(guess) != guess_length:
        guess = input(f"That wasn't {guess_length} chars! Try again: ")
    return guess


def main() -> None:  # this is where the game comes all together!
    """The entrypoint of the progrm and main game loop."""
    turn: int = 1  # how many turns the user has taken up.
    tries: int = 6  # total turns available to the user.
    secret: str = "codes"  # the secret word (for our purposes).
    while turn <= tries:  # this is the game loop! it lets the user take multiple guesses until "tries" is reached.
        print(f"=== Turn {turn}/{tries} ===")  # helps the user keep track of tries
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/{tries} turns!")  # lets the winner know they won!
            return
        else:
            turn += 1 
    print(f"X/{tries} - Sorry, try again tomorrow!")  # lets the winner know to try again another time!


if __name__ == "__main__": 
    main()