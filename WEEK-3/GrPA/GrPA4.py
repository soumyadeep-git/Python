s=input().lower()
a='abcdefghijklmnopqrstuvwxyz'
t=''
for x in a:
    for y in s:
        if x==y:
            t+=y
print(t)