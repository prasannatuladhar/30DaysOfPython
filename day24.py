"""
1) Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, raise a ValueError and inform them that their choice was invalid.

2) Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions, TypeError exceptions, and other kinds of ArithmeticError.

divide(a, b)
	print(a / b)
3) Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances of KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused this issue. Once you have written to the log file, reraise the original exception.

def itemgetter(collection, identifier):
	return collection[identifier]
    

"""

# 1 Solutions
user_input = int(input("Enter any number from 1 to 10 "))

if user_input  in range(1,11):
    print(f"Your number is {user_input}")
else:
    raise ValueError("Not in range")    

# 2 Solutions

def divide(a, b):
    try:
        result =  a/b
    except ZeroDivisionError:
        print("We cannot divide any number with zero")  
    except TypeError:
        print("Number cant be be divisible by letters")
    except ArithmeticError:
        print("Cant proceed further. Number is too large")    

    else:
        # print(result)
        print(round(result,2))

divide(54444,703)

# 3 Solutions

def log_exception(exception, fn, **kwargs):
	values = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
	
	with open("log.txt", "a") as log_file:
		log_file.write(f"Exception: {exception}, Function: {fn}, Values: {values}\n")
		

def itemgetter(collection, identifier):
	try:
		return collection[identifier]
	except (IndexError, KeyError, TypeError) as ex:
		log_exception(ex, "itemgetter", collection=collection, identifier=identifier)
		raise













