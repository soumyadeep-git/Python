a = input()
b = input()
for c in a:
    if c in b:
        b = b.replace(c,'')
print(b)