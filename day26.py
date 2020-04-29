"""
1) Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget.Prompt the 
 user to provide information for each of these fields and create an instance of the Movie tuple you defined.
2) Use a defaultdict to store a count for each character that appears in a given string. Print the most common 
character in this dictionary. 
3) Use the mul function in the operator module to create a partial called double that always provides 2 as
 the first argument.
4) Create a read function using a partial that opens a file in read ("r") mode  
 """
#  1 Solutions
from collections import namedtuple

Movie = namedtuple("Movie",["title","director","released_year","budget"])
title = input("Enter movie name :")
director = input("Enter director name :")
released_year = int(input("Enter released year :"))
budget = float(input("Enter budget of movie :"))

movie1 = Movie(title,director,released_year,budget)
print(f"The name of movie is {movie1.title} which is directed by {movie1.director} released in {movie1.released_year} with ${movie1.budget}")

# 2 Solutions
from collections import defaultdict

s = "prasanna"
letter_count = defaultdict(int)

for character in s:
	letter_count[character] += 1

most_common_character = max(letter_count, key=lambda key: letter_count[key])
print(most_common_character)

# 3 Solutions
def mul(a,b):
    return a*b
from functools import partial
double = partial(mul,2)
print(double(5))

# 4 Solutions
from functools import partial

read = partial(open,mode="r")


