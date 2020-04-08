# Below you'll find a list which contains the relevant data about a selection of movies. Each item in the list is a tuple containing a movie name and movie budget in that order:
# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 20000000),
#     ("Memento", 9000000),
#     ("Requiem for a Dream", 4500000),
#     ("Pirates of the Caribbean: On Stranger Tides", 379000000),
#     ("Avengers: Age of Ultron", 365000000),
#     ("Avengers: Endgame", 356000000),
#     ("Incredibles 2", 200000000)
# # ]
# For this project, your program should do the following:

# Calculate the average budget of all movies in the data set.
# Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
# Print out how many movies spent more than the average you calculated.
# If you want a little extra challenge, allow users to add more movies to the data set before running the calculations.

# You can do this by asking the user how many movies they want to add, which will allow you to use a for loop and range to repeat some code a given number of times. Inside the for loop, you can write some code that takes in some user input and appends a movie tuple containing the collected data to the movie list.
# 3 Print out how many movies spent more than the average you calculated.


# Solution
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
total_budget=0
movie_count=0
for mov in movies:
    total_budget += mov[1]
    movie_count += 1
# 1 solution   
avg_budget = total_budget/movie_count
print(f"Average budget of movie is {avg_budget}")

# 2 solution 
high_budget_count = 0  
for mov in movies:
    if mov[1]>avg_budget:
        print(f"list of high budget movies are {mov[0]}. Budget is {mov[1]-avg_budget} more than average budget")
        high_budget_count +=1

#3 Solution
print(f"There are {high_budget_count} movies who spent more than the average")        



 