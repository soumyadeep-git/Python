def factorial(n):
    if(n<0):
        return -1
    elif(n == 0):
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact*i
        return fact
