"""Creates several dictionary utility functions"""

__author__: str = "730756982"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts all values in a dictionary"""
    inverted_dictionary: dict[str, str] = {}
    for key in dictionary:
        # raises key error if inverting the dictionary causes duplicate key values
        if dictionary[key] in inverted_dictionary:
            raise KeyError("Cannot invert because of duplicate key values.")
        inverted_dictionary[dictionary[key]] = key  # inverts keys and values
    return inverted_dictionary


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the color that appears most in the dictionary"""
    num_appearances: dict[str, int] = {}
    count: int = 0
    if len(color_dict) != 0:
        # creates a new dictionary with the color and the number of times it appears
        for person in color_dict:
            if count == 0:
                # sets favorite colors equal to the first color in the list
                fav_color: str = color_dict[person]
            if color_dict[person] in num_appearances:
                # if color already in the dict, increases number of times by one
                num_appearances[color_dict[person]] += 1
            else:
                # if color not in the dict, intitializes the number of times to one
                num_appearances[color_dict[person]] = 1
            count += 1
        # sets favorite color to the color with the most appearances
        for color in num_appearances:
            if num_appearances[color] > num_appearances[fav_color]:
                fav_color = color
    else:
        fav_color = ""
    return fav_color


def count(a_list: list[str]) -> dict[str, int]:
    """Creates a dictionary with each element in a list and the
    number of times the element occurs in the list as key/value pairs"""
    counts: dict[str, int] = {}
    for item in a_list:
        # if the item is in the dictionary,
        # increases the number of times it occurs by one
        if item in counts:
            counts[item] += 1
        # if the item is not in the dictionary,
        # initializes the number of times it occurs to one
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Takes in a list and returns a dictionary with
    the first letter of the words in the list and a list of
    what words start with the letter"""
    # initialize new dictionary
    alphabet_dict: dict[str, list[str]] = {}
    # sets every first letter of the words in the list
    # equal to an empty list in the dictionary so
    # the words can be added to the list later
    for word in words:
        first_letter = word[0].lower()
        alphabet_dict[first_letter] = []
    # adds each word to the corresponding list
    # in the dictionary based on its first letter
    for word in words:
        first_letter = word[0].lower()
        alphabet_dict[first_letter].append(word)
    return alphabet_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """adds a student to a list of students in a dictionary that
    attended class on a certain day"""
    # if the day is already recorded in the dictionary,
    # the student is added to the list of students that attended that day
    if day in attendance:
        # if the student is not already in the list,
        # adds the student to the list
        if student not in attendance[day]:
            attendance[day].append(student)
    # if the day is not recorded in attendance yet, a new day is added
    # to the dictionary and the corresponding list of students is only
    # the one student
    else:
        student_list: list[str] = [student]
        attendance[day] = student_list
