#!/usr/bin/env python3
"""
Chopt
"""

import random
from random import randrange

__author__ = "pliggity"
__version__ = "0.1"
__license__ = "MIT"

chefs = ["Austin", "Amanda", "Darien", "Mariah", "Rico","Taylor"]
courses = ["Drinks", "Appetizer 1", "Main Course", "Dessert", "Side Dish", "Appetizer 2"]
ingredients = ["Avocado", "Mint", "Coffee", "Cilantro", "Quail Eggs", "Basil", "Salmon"]

def chopt_assign():

    random.seed()

    for chef in chefs:
        c = randrange(len(courses))
        i = randrange(len(ingredients))

        print(chef, " - ", courses[c], " - ", ingredients[i], "\n")

        courses.pop(c)
        ingredients.pop(i)


def main():
    chopt_assign()


    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

