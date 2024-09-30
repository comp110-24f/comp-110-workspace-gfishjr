from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

"""Imports the concat function and adds two strings using the function"""

__author__: str = "730756982"

# global variables
x: str = "123"
y: str = "abc"

# prints the results of concatenating x and y
print(concat(first_string=x, second_string=y))
# prints the coordinate pairs of x and y
get_coords(xs=x, ys=y)
