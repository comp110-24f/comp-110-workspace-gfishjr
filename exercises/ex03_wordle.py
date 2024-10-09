"""This program simulates the game Wordle, where the user has 6 tries
to guess a secret word"""

__author__: str = "730756982"

# named constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # sets the max number of guesses to 6
    max_guesses: int = 6
    # initializes the number of guesses to 1 and prints everything
    # that will happen after the first guess
    num_guesses: int = 1
    print("=== Turn " + str(num_guesses) + "/6 ===")
    guess = input_guess(secret_word_len=len(secret))
    print(emojified(guess=guess, secret=secret))
    while num_guesses < max_guesses and guess != secret:
        # continues to prompt the user for a guess until
        # either the user guesses the word or the max number
        # of guesses is reached
        num_guesses += 1
        print("=== Turn " + str(num_guesses) + "/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        print(emojified(guess=guess, secret=secret))
    # The loop exited because either the word was guessed or
    # the user ran out of guesses, so this if/else statement
    # determines which reason and prints the appropriate message
    if guess == secret:
        print("You won in " + str(num_guesses) + "/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Makes sure the guess is the same length as the secret word"""
    word = input("Enter a " + str(secret_word_len) + " character word: ")
    # loops until the user enters a word of the correct length
    while len(word) != secret_word_len:
        word = input("That wasn't " + str(secret_word_len) + " chars! Try again: ")
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks to see if a character occurs in a word"""
    assert len(char_guess) == 1
    index: int = 0
    # iterates through secret_word and returns true if char_guess
    # is equal to any of the characters in secret_word; otherwise
    # returns false
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a sequence of emojies based on whether each letter from
    guess is in the right place, in the word but in the wrong place,
    or not not in the word at all."""
    assert len(guess) == len(secret)
    # initializes the emoji string as blank
    emoji_string: str = ""
    index: int = 0
    # iterates through each character in guess and adds the
    # appropriate emoji to the string
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_string += f"{GREEN_BOX}"
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            emoji_string += f"{YELLOW_BOX}"
        else:
            emoji_string += f"{WHITE_BOX}"
        index += 1
    return emoji_string


# does not execute this code when the file is imported
if __name__ == "__main__":
    main(secret="codes")
