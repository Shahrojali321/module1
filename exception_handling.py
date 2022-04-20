"""Defination: To finf the division of a number """
def division_number(num1,num2):
    value=num1/num2
    return value
try:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the 2nd number:"))
    result=division_number(num1,num2)
    print(f"The result is:{result}")
except ZeroDivisionError as e:
    print("oops, you cannot divide the number by zero")
except ValueError as k:
    print("Invalid input")
except Exception as f:
    print("Something went wrong")
finally:
    print("resource closed")
