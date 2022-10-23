n = int(input())
# Accept matrix A
A = [ ]
for i in range(n):
    row = [ ]
    for x in input().split(','):
        row.append(int(x))
    A.append(row)
# Accept matrix B
B = [ ]
for i in range(n):
    row = [ ]
    for x in input().split(','):
        row.append(int(x))
    B.append(row)
# Initialize matrix C as a zero-matrix
C = [ ]
for i in range(n):
    row = [ ]
    for j in range(n):
        row.append(0)
    C.append(row)
# Matrix product
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
        if j != n - 1:
            print(C[i][j], end = ',')
        else:
            print(C[i][j])