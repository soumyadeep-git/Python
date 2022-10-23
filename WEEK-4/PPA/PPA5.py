x=input()
r=x.split(' ')
i = 0
s=''
while i<( len(r)-1) :
    n = int(float(r[i]))
    s += str(n)+','
    i += 1
n= int(float(r[i]))
s += str(n)
print(s)