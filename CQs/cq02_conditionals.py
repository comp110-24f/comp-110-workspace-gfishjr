"""This program is a simple number guessing game."""

__author__: str = "730756982"


def guess_a_number() -> None:
    """Tells the user whether their guess was right, too high, or too low."""
    secret: int = 7
    guess = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
