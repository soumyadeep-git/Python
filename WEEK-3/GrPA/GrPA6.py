n=int(input())
for i in range(1,n+2):
    for j in range(1,i):
        if j<i-1:
            print(j,end=',')
        else:
            print(j)
for i in range(n,0,-1):
    for j in range(1,i):
        if j<i-1:
            print(j,end=',')
        else:
            print(j)