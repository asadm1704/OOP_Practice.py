'''in thid module we will learn about 2D arrays in python
A 2D array is an array of arrays, where each element is itself an array.
We can create a 2D array using nested lists in Python.
For example:'''
# Creating a 2D array
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# no of rows 
rows = len(array_2d)
# no of columns
cols = len(array_2d[0]) # assuming all rows have the same number of columns of [0] index
# printing the 2D array
for i in range(rows):
    for j in range(cols):
        print(array_2d[i][j], end='   ')
    print()
print()   # for new line after each row
    # upper triangular matrix
for i in range(rows):
    for j in range(cols):
        if j>=i:
          print(array_2d[i][j], end='   ')
        else:
            print("* ", end=' ')
            
    print()
print()
# lower triangular matrix
for i in range(rows):
    for j in range(cols):
        if j<=i:
          print(array_2d[i][j], end='   ')
        else:
            print("* ", end=' ')
            
    print() 
print()
    #diagonal matrix
for i in range(rows):
    for j in range(cols):
        if j==i:
          print(array_2d[i][j], end='   ')
        else:
            print("* ", end=' ')
            
    print() 
print()
# transpose of matrix the rows become columns and columns become rows
transpose = [[0]*rows for _ in range(cols)] #create a 2D array initialized with zeros

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = array_2d[i][j]

for row in transpose:
    for val in row:
        print(val, end='   ')
    print()
    
#rotate a matrix by 90 degrees clockwise
#brute force approach
rotated = [[0]*rows for _ in range(cols)] #create a 2D array initialized with zeros
for i in range(rows):
    for j in range(cols):
        rotated[j][rows-1-i] = array_2d[i][j]
print()
for row in rotated:
    for val in row:
        print(val, end='   ')
    print()
    
#lets do it in place
