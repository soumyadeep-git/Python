x, y = 0, 0
str = input()
while str != "STOP":
    if str == "UP":
        y += 1
    if str == "DOWN":
        y -= 1
    if str == "LEFT":
        x -= 1
    if str == "RIGHT":
        x += 1
    str = input()

sum = abs(x) + abs(y)
print(sum)
    
