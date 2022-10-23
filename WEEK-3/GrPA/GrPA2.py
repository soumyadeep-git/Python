n = int(input())
cond = False
for i in range(2, n):
    count = 0
    if n % i == 0:
        cond = True #checking if i is a factor of n or not
        for j in range(2, i):
            if i % j == 0: # 5 % 2
                count += 1
        if count == 0:
            print(i)
if not cond:
    print(n)