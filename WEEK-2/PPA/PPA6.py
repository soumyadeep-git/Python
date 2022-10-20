a = input()
if len(a)%2 ==0:
    if a[-1] == ".":
        a = a[:-1]
    else:
        a = a+"."
    c = len(a)//2
    print(a[c-1:c+2])
else:
    c = len(a)//2
    print(a[c-1:c+2])