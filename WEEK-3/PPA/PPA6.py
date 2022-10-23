
str = input()
final_str = str
while str!= "abcdefghijklmnopqrstuvwxyz":

    if len(str)<len(final_str):
        final_str = str
    str = input()
print(final_str)