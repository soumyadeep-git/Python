matrix=[]
n=int(input())
for i in range(n):
    f=input().split(' ')
    for j in range(n):
        f[j]=int(f[j])
    matrix.append(f)

print(matrix)