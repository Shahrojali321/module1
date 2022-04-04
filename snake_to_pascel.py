"""defination:To convert the Snake notation to Pascel notation"""
    
def snake_case(str):
    """To convert the Snake notation to Pascel notation"""
    sc=str.split("_")
    for i in range(len(sc)):
        sc[i]=sc[i].capitalize()
    return "".join(sc)
input=input("Enter the snake_case:")
result=snake_case(input)
print(f"Pascel case is: {result} ")
