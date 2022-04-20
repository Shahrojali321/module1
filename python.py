"""Defination:To find the file of particular extension"""
import os
#import re
path = 'D:/pratice/module01/XML'
def file_name(path,pattern):
    """To find the file of particular extension"""
    a=[]
    for filename in os.listdir(path):
        if not filename.endswith(pattern):
            continue
    #fullname = os.path.join(path, filename)
        a.append(filename)
    return a
pattern=input("Enter the type of file you want:")
result=file_name(path,pattern)
print(f" The file is :{result}")