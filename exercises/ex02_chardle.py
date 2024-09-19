"""This program takes a five letter word and a letter from the user,
and then outputs the indices where the letter is found in the word
as well as how many times it is found in the word."""

__author__: str = "730756982"


def main() -> None:
    """calls the contains_char function with the input_word
    function and input_letter function as arguments"""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Asks the user for a 5 letter word and returns it if is the correct length"""
    word = input("Enter a 5-character word: ")
    # prints an error message if the word is not five characters and exits the program
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Asks the user for a single character and returns it if is the correct length"""
    letter = input("Enter a single character: ")
    # prints an error message if the string is not one character and exits the program
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """Counts the number of times the letter appears in the word
    and at which indices"""
    print("Searching for " + letter + " in " + word)
    index: int = 0
    count: int = 0
    # While loop iterates through the word
    while index < len(word):
        if word[index] == letter:
            # if the letter is equal to word at that index, count is increased by one
            count += 1
            print(letter + " found at index " + str(index))
        index += 1
    # prints how many instances of the letter were found in word
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# calls the main function
if __name__ == "__main__":
    main()
