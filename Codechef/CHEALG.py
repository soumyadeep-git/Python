
for _ in range(int(input())):
    s=str(input())
    news=""
    i=0
    n=0
    while i < len(s):
        n=1
        while (i+n < len(s) and s[i] == s[i+n]):
            n = n + 1
        news=news+s[i]+str(n)
        i=i+n
        
    if len(news)<len(s):
        print("YES")
    else:
        print("NO")