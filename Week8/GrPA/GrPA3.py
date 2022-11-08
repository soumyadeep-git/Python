def collatz(n):
    if n==2:
        return 1
    else:
        if n%2!=0:
            c=1+collatz((3*n)+1)
            return c
        else:
            c=1+collatz(n/2)
    return c