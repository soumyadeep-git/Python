
x =  float(input())
y =  float(input())
if(x==0 and y==0):
    print("origin")
elif(x ==0 and y!=0):
    print("y-axis")
elif(y ==0 and x!=0):
    print("x-axis")
elif(x > 0 and y >0):
    print("first")
elif(x < 0 and y >0):
    print("second")
elif(x < 0 and y <0):
    print("third")
elif(x > 0 and y <0):
    print("fourth")