""" 1) Write a function that prompts the user for their name and then greets them. You should process the string by removing any whitespace and 
 converting the string to title case.
If after processing the string you're left with an empty string, the function should replace the empty string with "World" in the output.
2) Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper or lowercase).
3) Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 (inclusive). Sort each
 of these lists into descending order (largest first), and then truncate each list so that only 5 items remain in each.
"""



# # 1 Solutions
name = input("Enter your name ").strip().title() or "World"
if name:
    print(f"Hello {name}")

# 2 Solutions
from string import ascii_letters
def check_for_ascii(something):
    for char in something:
        if char not in ascii_letters:
            return False
    else:
        return True

print(check_for_ascii("or?s/?sasdas"))     

# 3 Solutions
import random
numbers = range(1,101)
sample_list = [[sorted(random.sample(numbers,15),reverse=True)] for _ in range(3)]
# print(*sample_list[0][:5])
for s_list in sample_list:
    print(s_list[0][:5])
