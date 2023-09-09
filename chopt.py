#!/usr/bin/env python3
"""
Chopt
"""

import random
from random import randrange

__author__ = "pliggity"
__version__ = "0.1"
__license__ = "MIT"

chefs = ["Austin", "Amanda", "Darien", "Maryan", "Taylor"]
courses = ["Beverage", "Main Course", "Dessert", "Side", "Appetizer"]
ingredients = ["Lemon", "Lime","Cinnamon","Graham cracker","Corn","Powdered sugar","Potatoes","Ground meat","Beer","Twinkies","Onion","Strawberries","Stick o' butter","Bacon","Mushrooms","Marshmallow",
"Chocolate","Peach","Pizza","Turkey leg","Oreos", "Red Bull","Cheese curds","Corn bread","Hot dog","Panko","Radishes", "Pumpkin","Squash","Caramel apple"]

# opening the file in read mode
tv_shows_file = open("tv_shows.txt", "r")
  
# reading the file
data = tv_shows_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
tv_shows = list(set(data_into_list))
tv_shows_file.close()

def chopt_assign_ingredient():

    random.seed()

    for chef in chefs:
        c = randrange(len(courses))
        i = randrange(len(ingredients))

        print(chef, " - ", courses[c], " - ", ingredients[i], "\n")

        courses.pop(c)
        ingredients.pop(i)


def chopt_assign_tv_show():
    random.seed()
    for chef in chefs:
        c = randrange(len(courses))
        i = randrange(len(tv_shows))

        print(chef, " - ", courses[c], " - ", tv_shows[i], "\n")

        courses.pop(c)
        tv_shows.pop(i)


def main():
    chopt_assign_tv_show()
    #chopt_assign()


    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
