L = input().split(',')
m = " "
max = 0
for i in range(len(L)):
    if len(L[i]) >= max:
        max = len(L[i])
        m = " "
        m = m + L[i]
print(m)