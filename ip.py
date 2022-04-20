"""Defination: To find the ip address """
import re
file=["10.10.10.10","0.0.0.0","153.10.0.10","abcd"]  
"""To find the ip address"""
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
address=0
def ip(i):
  lst=[]
  for i in file:
    if pattern.search(i):
      lst.append(i)
  return lst
result=ip(address)    
# displaying the extracted IP addresses
print(f"The ip address is:{result}")