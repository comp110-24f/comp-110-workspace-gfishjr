"""My first challenge question where I write a function."""

__author__ = "730756982"


def mimic(message: str) -> str:
    """This function takes input and repeats it back."""
    return message


def main() -> None:
    """Prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
