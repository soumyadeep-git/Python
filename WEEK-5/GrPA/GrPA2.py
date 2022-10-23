def is_perfect(num):
    # Factor sum
    fsum = 0
    for i in range(1, num):
        if num%i == 0:
            fsum = fsum + i
    return num == fsum
print(is_perfect(int(input())))