# Reverse every kth row in a matrix

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    matrix.append(row)

k = int(input("Enter k: "))

# Reverse every kth row
for i in range(k - 1, r, k):
    matrix[i].reverse()

print("Matrix after reversing every kth row:")

for row in matrix:
    print(row)
