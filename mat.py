row = int(input("Enter rows number: "))
column = int(input("Enter columns number: "))
matrix = []
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
for i in range(row):
    for j in range(column):
        print(matrix[i][j] , end = " ")
    print()
