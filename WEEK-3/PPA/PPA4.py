n = int(input())
count = 0
for i in range(1, n+1):
    if(n%i ==2):
        count = count+1
if count>2:
    print("NOTPRIME")
else:
    print("PRIME")