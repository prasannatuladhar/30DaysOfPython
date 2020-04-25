"""
1) Below you'll find a list containing several tuples full of numbers:

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
2) Use the map function to find the sum of the numbers in each tuple. Use manual iteration to print the first two results provided by the resulting map object.

3) Imagine you have 3 employees and it's been agreed that the employees will take it in turns to lock up the shop at night. This means that for employees A, B, and C, employee A will close the shop on day 1, then B will close the shop on day 2, C will close the shop on day 3, and then we start the cycle again with employee A.

Write a program to create a schedule that lists which of your employees will lock up the shop on a given day over a 30 day period. You should list the day number, the employee name, and the day of the week. You can choose any employee to lock the shop on day 1, and you can also choose which day of the week day 1 corresponds to.
"""



# 2 Solutions
numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
list1 = map(lambda num: sum(num),numbers)
print(next(list1))
print(next(list1))

# 3 Solutions
employee = ["Emp A","Emp B","Emp C"]
employee10 = employee*10
days = list(range(1,31))
schedule= zip(employee10,days)
for shift in schedule:
    print(shift)


# using itertool

import itertools

employees = itertools.cycle(["Peter", "Fiona", "Carl", "Helen"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for day_number in range(1, 31):
	print(f"Day {day_number} ({next(days)}): {next(employees)} closes.")    
