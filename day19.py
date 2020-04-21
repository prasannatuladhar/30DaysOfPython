# Exercises
# 1) Create a short program that prompts the user for a list of grades separated by commas.
#  Split the string into individual grades and use a list comprehension to convert each string to an integer.
#  You should use a try statement to inform the user when the values they entered cannot be converted

# 2) Investigate what happens when there is a return statement in both the try clause and finally
#  clause of a try statement.

# 3) Imagine you have a file named data.txt with this content:

# There is some data here!
# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.

# When files don't exist when you try to open them, the exception raised is FileNotFoundError.

# 1 Solutions
try:
    marks = input("Enter a your each marks with comma :")
    formated = marks.split(',')
    result =  [int(grade) for grade in formated]
    print(result)
except ValueError:
    print("Sorry you have not correctly given input")    

# 2 Solutions    
def sum_of_two_numbers():
    try:
        num1 = int(input("Enter a first number :"))
        num2 = int(input("Enter a Second number :"))
        return num1+num2   #this gets ignore because of finally

    except ValueError:
        print("Sorry that is not number. Cant sum")  

    finally:
        return num1*num2

print(sum_of_two_numbers())

# 3 Solutions
try:
    with open('data.txt','r') as my_file:
        data= my_file.read()
        print(data)
except FileNotFoundError:
    print("File doest not exist dude")        


