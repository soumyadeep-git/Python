def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        f=0
        f=fibo(n-1)+fibo(n-2)
        return f