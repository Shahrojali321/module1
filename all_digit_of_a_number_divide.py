"""Defination: To Check if all digits of a number divide it. """
num=0
def check_divisibility(num,digit):
    return (digit != 0 and num % digit ==0)
#Function to check if all digits of num divide it or not
def all_digits_divide(num): 
    temp = num
    while (temp > 0) :
        digit = temp % 10
        if((check_divisibility(num, digit)) == False) :
            return False
        temp = temp // 10 
    return True
num=int(input("enter the number:")) 
if (all_digits_divide(num)) :
    print("Yes")
else :
    print("No")