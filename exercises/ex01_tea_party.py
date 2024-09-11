""" Calculates the number of tea bags and treats, as well as cost for a
    tea party based on the number of guests """

__author__: str = "730756982"


def main_planner(guests: int) -> None:
    """Outputs the number of tea bags and treats and the cost based on
    the number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """calculates the number of tea bags based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """calculates the number of treats based on the number of tea bags"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the total cost of the tea and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
