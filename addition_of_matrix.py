"""defination:To find Addition of two matrix"""
def matrix(m,n):
    """To find Addition of two matrix"""
    outer_matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter outer_matrix[{i}][{j}]"))
            row.append(inp)
        outer_matrix.append(row)
    return outer_matrix
def sum(matrix1,matrix2):
    output = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        output.append(row)
    return output
m=int(input("Enter the value of m:\n"))
n=int(input("Enter the value of n:\n"))
print("Enter the matrix1")
matrix1=matrix(m,n)
print(matrix1)
print("Enter the matrix2")
matrix2=matrix(m,n)
print(matrix2)
result=sum(matrix1,matrix2)
print(f"sum of the two matrix is:{result}")
