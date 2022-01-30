"""One-shot wordle: another cute step towards Wordle."""

__author__ = "730469821"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

match_guess_index = 0
emoji_guess_index: str = ""

while len(guess) != len(secret_word):
    guess: str = input("That was not 6 letters! Try again: ")

while match_guess_index < len(secret_word):
    if guess[match_guess_index] == secret_word[match_guess_index]:
        emoji_guess_index = emoji_guess_index + GREEN_BOX
    else:
        guess_character_present: bool = False
        secret_alt_ind = 0

        while guess_character_present is not True and secret_alt_ind < len(secret_word):
            if secret_word[secret_alt_ind] == guess[match_guess_index]:
                guess_character_present: bool = True
            else:
                secret_alt_ind = secret_alt_ind + 1
        if guess_character_present is True:
            emoji_guess_index = emoji_guess_index + YELLOW_BOX
        else:
            emoji_guess_index = emoji_guess_index + WHITE_BOX
    match_guess_index = match_guess_index + 1


print(emoji_guess_index)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")