# cook your dish here

for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    cnt = 0
    for i in range(0,n):
        sumi = 0
        pro  = 1
        for j in range(i,n):
            sumi += l[j] 
            pro  *= l[j] 
            
            if sumi == pro:
                cnt += 1 
    print(cnt)