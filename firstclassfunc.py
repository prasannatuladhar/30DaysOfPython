def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b    

def div(a,b):
    if b==0:
        print("Cant do division on 0")
    else:
        return a/b

operations = {
    "a":add,
    "s":sub,
    "m":mul,
    "d":div
}        

selection = input(""" Select
  a for Addition,
  s for sub,
  d for division,
  m for multiplication """
)

operation = operations.get(selection)
if operation:
    a = int(input("Enter a value for a:"))
    b = int(input("Enter a value for b:"))
    print(operation(a,b))
else:
    print("Invalid selection")