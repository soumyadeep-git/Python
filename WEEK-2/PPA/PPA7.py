a = input()
b = input()
c = input()
d = input()
e = input()
count = 0
if a in b:
    if b in c:
        if c in d:
            if d in e:
                count = 1
if count ==1:
    print("magical")
else:
    print("non-magical")