"""This program simulates the game Wordle, where the user has 6 tries
to guess a secret word"""

__author__: str = "730756982"

# named constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    """Makes sure the guess is the same length as the secret word"""
    word = input("Enter a " + str(secret_word_len) + " letter word: ")
    while len(word) != secret_word_len:
        word = input("That wasn't " + str(secret_word_len) + " chars! Try again: ")
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks to see if a character occurs in a word"""
    assert len(char_guess) == 1
    index: int = 0
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
    emoji_string: str = ""
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_string += f"{GREEN_BOX}"
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            emoji_string += f"{YELLOW_BOX}"
        else:
            emoji_string += f"{WHITE_BOX}"
        index += 1
        emoji_string += " "
    return emoji_string
