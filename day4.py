# Day 4 List and Tuples
# 1.Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
# 2.Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
# 3.Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
# 4.Use an f-string to print the movie name and release year by accessing your new movie tuple.
# 5.Add the new movie tuple to the movies collection using append.
# 6.Print both movies in the movies collection.
# 7.Remove the first movie from movies. Use any method you like.


# Solution 1
movie_collection =[('Avatar','Christopher Nolan',2018,45000)]

# Solution 2
title=input("Enter a title of movie ")
director_name=input("Enter a Director of movie ")
released_year=int(input("Enter a Released Year of movie "))
movie_budget=float(input("Enter a Budget of movie "))

# Solution 3
tuple_list=(title,director_name,released_year,movie_budget)

# Solution 4
print(f"Movie Name:{tuple_list[0] },Released Year:{tuple_list[2]}")

# Solution 5
movie_collection.append(tuple_list)

# Solution 6
print(movie_collection)

# Solution 7
del movie_collection[0]
print(movie_collection)

