GAA = int(input("GAA: "))
Qz1 = int(input("qz1: "))
F = int(input("F: "))
PE1 = int(input("PE1: "))
PE2 = int(input("PE2: "))


T1 = 0.1 * GAA + 0.1 * Qz1 + 0.5 * F + 0.2 * max(PE1, PE2)
T2 = 0.1 * GAA + 0.1 * Qz1+ 0.4 * F + 0.3 * max(PE1,PE2) + 0.1 * min(PE1,PE2)

print(T1)
print(T2)

if T1 > T2:
    print("Best Result:", T1)
else:
    print("Best Result:", T2)