n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            if(j==(n-1)):
                print('1')
            else:
                print('1',end=',')
        else:
            if(j==(n-1)):
                print('0')
            else:
                print('0',end=',')