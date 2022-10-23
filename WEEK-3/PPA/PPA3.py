a = int(input())
b = int(input())
output = 0
for i in range(1000,2001):
    if(i%a ==0 and i%b ==0):
        output = output+i
print(output)