num_list = [1,4,5,6,2,4,3]
for index,num in enumerate(num_list):
    if index % 2==0:
        num = num*2
    print(f"{index} ,{num} ")
    