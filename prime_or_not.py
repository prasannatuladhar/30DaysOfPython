#get a number and find prime or not using For loop
num = int(input("enter a number :"))

for divider in range(2,num):
    if num%divider==0:
        print("This is not Prime Number")
        break
else:
    print(f"The {num} is prime number")    


#get a number and find prime or not using While loop
new_num=int(input("Enter a number "))
divisor_num=2
while new_num>divisor_num:
    if new_num%divisor_num==0:
        print(f"This number {new_num} is not prime")
        break
    divisor_num += 1
else:
    print(f"This number {new_num} is prime")    



