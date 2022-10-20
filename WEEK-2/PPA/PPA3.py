time = float(input())
if(time<0 or time>=24):
    print("INVALID")
elif(time>=0 and time<=5):
    print("NIGHT")
elif(time>=6 and time<=11):
    print("MORNING")
elif(time>=12 and time<=17):
    print("AFTERNOON")
elif(time>=18 and time<=23):
    print("EVENING")
# elif(time>=24):
#     print("INVALID")

