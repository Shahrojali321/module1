""""Defination:To find the sum of all items in a dictionary"""
def sum_dic(dictionary):
    """To find the sum of all items in a dictionary"""
    return sum(dictionary.values())
dict={}
for i in range(int(input("enter dictionary length"))):
    a=input("key")
    b=int(input("value"))
    dict[a]=b
result=sum_dic(dict)
print(f"The sum of the value of Dictonary:{result}")
    
    