"""
1) Import the fractions module and create a Fraction from the float 2.25. You can find information on how to create fractions in the documentation.

2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function. You can find documentation for this function here.

4) Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.
"""

# 1 Solutions
from fractions import Fraction
num_in_fraction = Fraction(2.25)
print(num_in_fraction)

# 2 Solutions
from math import fsum
numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))
# print(sum(numbers))

# 3 Solutions
from random import randint 
rand_num = randint(1,100)
print(rand_num)

# 4 Solutions
computer_guess_number = randint(1,10)
user_num = int(input("Enter a number between 1 to 10 :"))
while True:
    if user_num > computer_guess_number:
        print("Your number is higher than Computer Guessing")
        user_num = int(input("Enter a number again between 1 to 10 :"))
    elif user_num < computer_guess_number:
        print("Your number is lower than Computer Guessing")
        user_num = int(input("Enter a number again between 1 to 10 :"))
    else:
        print("Congrats! you made a right guess")  
        break

  
