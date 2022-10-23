num = input().split(",")
l = []
max = -1
for i in range(len(num)):
    if int(num[i])> max:
        max = int(num[i])
print(max)
