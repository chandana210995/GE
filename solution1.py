rows= int(input("Enter number of rows\n"))
columns= int(input("Enter number of columns\n"))
matrix =[]
for i in range(rows):
    temp=[]
    for j in range(columns):
        print ('Enter the value of matrix position [',(i+1), ',' ,(j+1), '].')
        temp.append(input())
    matrix.append(temp)
print("Enter the column position to be displayed. i.e, value should be less than", columns,".")
c=int(input())-1
for i in range(rows):
      print(matrix[i][c], end="\0")
print ("\nEnter the row position to be displayed. i.e, value should be less than", rows,".")
r=int(input())-1
for i in range(columns):
      print(matrix[r][i], end="\0")
print ("\nEnter the quadrant position to be displayed. i.e, value of row and column should be less than", rows-1, ',' ,columns-1,".")
r=int(input())-1
c=int(input())-1
d=c
for i in range(2):
    for j in range(2):
        print(matrix[r][c], end="\0")
        c=c+1
    r=r+1
    c=d
