def write_pattern(n):
    f = open('pattern.csv', 'w')
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                f.write('1')
            else:
                f.write('0')
            if j != n - 1:
                f.write(',')
        if i != n - 1:
            f.write('\n')
    f.close()