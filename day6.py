# 1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.
# employees = [
#     ("Rolf Smith", 35, 8.75),
#     ("Anne Pun", 30, 12.50),
#     ("Charlie Lee", 50, 15.50),
#     ("Bob Smith", 20, 7.00)
# ]
# 2) For the employees above, print out those who are earning an hourly wage above average.
# Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.

# 1 Solution
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employe in employees:
    print(f"{employe[0]} will be paid {employe[1]*employe[2]}")

# 2 Solution   
num_of_emp = 0
total_wage = 0
  
for emp in employees:
    num_of_emp += 1
    total_wage += emp[2]
print(num_of_emp)   
print(total_wage)   
avg_income = total_wage/num_of_emp
print(avg_income)

for emp in employees:
    if emp[2] > avg_income:
        print(f"{emp[0]} earning is more than Average {emp[2]}")