# 1.Ask the user for their name and age, assign theses values to two variables, and then print them.
# 2.Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.
# 3.Below you’ll find some code with a number of errors. Try to go through the program line by line and fix the issues in the code. I’d encourage you to try running the program while you’re working on it, as reading the error messages is great practice for debugging your own programs.
# hourly_wage = input("Please enter your hourly wage: ')

# prnt("Hourly wage: ")
# print(hourlywage)
# print("Hours worked: ")
# print(hours_worked)

# hours_worked = input("How many hours did you work this week? ")



# 1 
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Your name is {name} and your age is {age} ")

# 2 After assiging with other variable
name="Tiger"
print(name)

# 3
hourly_wage = input("Please enter your hourly wage: ")
print(f"Hourly wage:{hourly_wage}")
hours_worked = input("How many hours did you work this week? ")
print(f"Hours worked: {hours_worked}")

