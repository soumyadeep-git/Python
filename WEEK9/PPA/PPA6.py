def write_AP(a_1, d, n):
    f = open('out.txt', 'w')
    x = a_1
    for i in range(n):
        line = f'{x}'
        if i != n - 1:
            line = line + '\n'
        f.write(line)
        x = x + d
    f.close()