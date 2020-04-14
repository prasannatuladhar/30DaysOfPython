"""
Exercises
1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.

2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.

3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:
("Tom Hardy", "English", 42)  # name, nationality, age
You can choose whatever key names you like for the dictionary.

4) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.
"""

# 1 Solutions

def exponentiate(a,b):
    return a**b

print(exponentiate(5,2))    

# 2 Solutions
def process_string(sth):
    return sth.lower().strip()

print(process_string("  Prasanna Tuladhar "))

#3 Solutions
def tup_to_dict(tup_value):
    name, nationality, age = tup_value
    return {
        'name':name,
        'nationality':nationality,
        'age':age
    }            
print(tup_to_dict(("Tom Hardy", "English", 42)))

# 4 Solutions
def is_prime(num):
    for n in range(2,num):
        if num % n == 0:
            return False
            break  
    else:
        return True         
print(is_prime(23))
