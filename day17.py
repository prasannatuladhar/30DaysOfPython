"""
1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.

2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

3) Print the following dictionary using the format method and ** unpacking.

 country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
 }
4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for print function's sep parameter for this exercise.

5) Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.
"""

# 1 Solutions
def sum_to_any_num(*anynum):
    return sum(anynum)

print(sum_to_any_num(2,4,5))    

# 2 Solutions

def prnt_info(*name,**info):
    for n in name:
        print(f"Namaste! {n}")

    for k,v in info.items():
        print(f"{k.title()}:{v}")


  
prnt_info("Prasanna","Ram","Mahesh",
occupation="Engineer",
age=36,
gender="Male")

#3 Solutions
country = {
	"name": "Germany",
	"population": "83 million",
	"capital": "Berlin",
	"currency": "Euro"
}
template = """
Name:{name},
Population:{population},
Capital:{capital},
Currency:{currency}

"""
print(template.format(**country))

#4 Solutions
# def print_to_20(*num):
#     print(num)
# print_to_20(*range(1,21))

print(*range(1,21),sep=",")

#5 Solutions
print(*range(1,21),sep="\n")