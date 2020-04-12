"""
Exercises
1) Create an empty set and assign it to a variable.

2) Add three items to your empty set using either several add calls, or a single call to update.
3) Create a second set which includes at least one common element with the first set.

4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.

"""

# 1 Solution
set_var=set()
print(type(set_var))

#2 Solution
set_var.add("item1")
set_var.update(["item2","item3"])
print(set_var)


#3 Solution
set_var2 = {"item1","item5","item6","item8"}

#4 Solution
uni_set=set_var.union(set_var2)
print(uni_set)
sym_diff_set=set_var.symmetric_difference(set_var2)
print(sym_diff_set)
intersec_set=set_var.intersection(set_var2)
print(intersec_set)

#5 Solution (Since set is immutable we are goint to solve using list)
set_num=[]
for num in range (5,11):
    set_num.append(num)

print(set_num)    
user_input = int(input("Enter a number: "))
print(user_input)
if user_input in set_num:
    print("Yess")
else:
    if user_input > set_num[0]:
        print("Number you have guessed is higher")
    else:
        print("Number you have guessed is lower")    
    
    