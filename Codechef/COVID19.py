for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    cov,count=[],1
    for i in range(n-1):
        if x[i+1]-x[i]<=2:
            count+=1 
        else:
            cov.append(count)
            count=1
        if i==n-2:
            cov.append(count)
    print(min(cov), max(cov))