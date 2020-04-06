# 1.Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.

# 2. Try to use the is operator or the id function to investigate the difference between this:
# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]
# And this:
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

# 4) Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.




# 1 Solution
name = [1,2,3]
new_name = [1,2,3]
print(name == new_name)
print(name is new_name)

#2 Solution
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

numbers = [1, 2, 3, 4]
numbers.append(5)

print(id(numbers)==id(new_numbers))
print(numbers is new_numbers)
print(numbers == new_numbers)

# 3 Solution
num=int(input("Enter a number "))
if num==0:
    print("The number you have typed is Zero")
elif num%2==0:
    print("The number you have typed is Even number")
else:
    print("The number you have typed is Odd number")    


# 4 Solution
hour_work = int(input("How many hour do you work "))
wage = int(input("How much do you get per hour from your job "))

if hour_work > 40:
    additional_hour_work = hour_work-40
    wage = wage*40 + additional_hour_work*wage*1.1
else:
    wage = wage*hour_work

print(f"Your total Salary is {wage}")         

