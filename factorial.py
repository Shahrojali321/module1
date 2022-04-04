"""description: To find the factorial of a number"""
def factorial(num):
    """To find the factorial of a number""" 
    fact = 1
    if num < 0:
        print("sorry, factorial does not exits for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            fact=fact*i
        return fact
#number=int(input("enter the number:"))
for number in range(1,10):
    result=factorial(number)
    print(f"The factorial of {number} is {result}")
