# Accept a positive integer nn as input and print all the factors of nn, one number on each line.
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        print(i)