"""description: To find the reverse of a input."""
def reverse(arr):
    """To find the reverse of input"""
    flag=False
    if arr[0]=="-":
        flag=True
        arr=abs(int(arr))
    lst=[x for x in str(arr)]
    i=0
    j=len(lst)-1
    while i<=j/2:
        lst[i],lst[j]=lst[j],lst[i]
        i+=1
        j-=1
    if flag==True:
        lst.insert(0,"-")
        return "".join(lst)
    else:
        return "".join(lst)

input=input("Enter the input : ")
result=reverse(input)
print(f"Output in {result}")