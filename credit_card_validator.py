input_card_num = input("Enter your card Number ") 
card_num = list(input_card_num)
if card_num[len(card_num)-1] == " ":
    card_num.pop()
    
if card_num[0] == " ":
    del card_num[0]


final_input_needed = []
for number in card_num:
    if number == " ":
        print("You did not entered number correctly ! Please type again")
        number = input("Enter your card Number ") 
        break
        
    else:
        final_input_needed.append(number)
print(final_input_needed)        

# ****************Second Part of Qsn*******************

last_num = final_input_needed.pop()
# print(final_input_needed)
rev_num=final_input_needed[::-1]
# print(rev_num)
sq_list=[]
rev_num = list(map(int, rev_num))
for index,num in enumerate(rev_num):
    if index%2==0:
        num = num*2
        if num > 9:
            num = num - 9
    sq_list.append(num)
final_value=sum(sq_list)+int(last_num)
print(final_value) 
if final_value%10==0:
    print("Your card is Proper and Valid ")
else:
    print("Sorry ! Your card is not valid")    


"""
Question
1) It should be able to accept a card number from the user. For this project, you can assume that the number will be entered as a single string of characters (i.e. there won't be any spaces between the numbers). However, you should be able to accept a card number with spaces at the start or end of the string.

If you want to challenge yourself, you should try to be more versatile with regards to the format that you accept card numbers in.

You may want to turn the user's input into a list of numbers, as that will make it easier to work with.

2) The program should validate that card number using the Luhn algorithm described above. You should implement this algorithm yourself.

After removing the checking digit and reversing the card number, you'll need a for loop to go over the credit card numbers. As you go through each digit, you must find a way to determine whether a digit is in an odd or an even position. Remember you can check the model solution if you get stuck!

3) Once the validation is complete, the program should inform the user whether or not the card number is valid by printing a string to the console.
"""    














        
