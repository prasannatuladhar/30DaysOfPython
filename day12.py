"""
Exercises
1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.

You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you should print a warning instead of calculating their division.

2) Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:

 tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
 }
 
 print_show_info(tv_show)
The print_show_info function should print the information stored in the dictionary, in a nice way. For example:

 Breaking Bad (2008) - 5 seasons
Remember you must define your function before calling it!

3) Below you’ll find a list containing details about multiple TV series.

 series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]
Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format.

4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.
"""


# 1.Solution 
def add(x,y):
    return x+y
def mul(x,y):
    return x*y   
def sub(x,y):
    return x-y  
def div(x,y):
    if y is 0:
        print("Can't perform calculation on Zero")
    else:
        return x/y           
    

print(add(3,2))   
print(mul(3,2))    
print(sub(3,2))    
print(div(0,3))    

# 2.Solution
tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
 }
 
def print_show_info(x):
    print(f"{x['title']} ({x['initial_release']}) - {x['seasons']} seasons")
    
print_show_info(tv_show)

# 3 Solution
series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]
 
def print_show_info1(x):
    for num in range(0,len(x)):
        print(f"{x[num]['title']} ({x[num]['initial_release']}) - {x[num]['seasons']} seasons")
    
print_show_info1(series)        

#4 Solutions
lis=[]
def palindrom_checker(inp):
    for n in str(inp):
        lis.append(n.lower())
        rev=lis[::-1]
    if lis == rev:
        print(f"{inp} is Palindrome")
    else:
        print(f"{inp} is Not Palindrom")      
    

palindrom_checker(1110111)