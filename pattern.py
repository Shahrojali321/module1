"""Defination: To print the pattern"""
def pattern(n):
    """To print the pattern"""
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n):
            print("*",end=" ")
        print("\n")
rows=int(input("Enter the number of rows:"))
result=pattern(rows)
print(f'The pattern is:{result}')