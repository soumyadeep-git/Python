first_side = int(input())
second_side = int(input())
third_side = int(input())

if first_side>=second_side and first_side>=third_side:
    third_side , first_side= first_side, third_side

elif second_side>=first_side and second_side>=third_side:
    third_side, second_side = second_side, third_side
if((third_side**2) == (first_side**2)+(second_side**2)):
    print("YES")
else:
    print("NO")