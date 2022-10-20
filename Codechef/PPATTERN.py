# cook your dish here
for _ in range(int(input())):
    n=int(input())
    p,q=1,n-1
    for i in range(n):
        t=p
        l=q
        for j in range(n):
            if (i+j)>l:
                t+=l
                l-=1
            else:
                t+=(i+j)
            print(t,end=' ')
        print()
        p+=(i+1)