# 1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.
# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.
# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.

# Solution 1
from random import randint
computer_guessing=randint(1,100)
print(computer_guessing) #just to track the guess
user_guess=int(input("Enter a number between 1 to 100 "))
while True:
    if user_guess > computer_guessing:
        print("Your guess is higher than Computer guess")
        user_guess = int(input("Guess again  between 1 to 100 "))
    elif user_guess < computer_guessing:
        print("Your guess is lower than Computer guess")
        user_guess = int(input("Guess again  between 1 to 100 "))
    else:
        print("You finally made a Right guess :) ")   
        break  

# Solution 2
for letter in "Python":
    if letter == 'o' or letter =='O':
        continue
    print(letter)

# Solution 3
list_prime =[]
for given_number in range(2,1000):
    for num in range(2,given_number):
        if given_number%num == 0:
            break
    else:
        list_prime.append(given_number)
print(list_prime)   
      

   


