"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730469821"


word_input = str(input("Please enter a 5-character word: "))
if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character_input = str(input("Please enter a single character: "))
if len(character_input) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character_input + " in " + word_input)

number_of_matches = 0

if str(word_input[0]) == character_input:
    print(character_input + " found at index 0")
    number_of_matches = number_of_matches + 1
  
if str(word_input[1]) == character_input:
    print(character_input + " found at index 1")
    number_of_matches = number_of_matches + 1

if str(word_input[2]) == str(character_input):
    print(character_input + " found at index 2")
    number_of_matches = number_of_matches + 1

if str(word_input[3]) == character_input:
    print(character_input + " found at index 3")
    number_of_matches = number_of_matches + 1

if str(word_input[4]) == character_input:
    print(character_input + " found at index 4")
    number_of_matches = number_of_matches + 1

if number_of_matches == 1:
    print(str(number_of_matches) + " instance of " + character_input + " found in " + word_input)
else:
    if number_of_matches > 1:
        print(str(number_of_matches) + " instances of " + character_input + " found in " + word_input) 
    else:
        print("No instances of " + character_input + " found in " + word_input)