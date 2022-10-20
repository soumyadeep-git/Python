# cook your dish here
t = int(input())
for _ in range(t):
    front = input()
    back = input()
    if (front[0]=='o' or back[0]=='o') and (front[1]=='b' or back[1]=='b') and (front[2]=='b' or back[2]=='b'):
        print('yes')
    elif (front[1]=='o' or back[1]=='o') and (front[2]=='b' or back[2]=='b') and (front[0]=='b' or back[0]=='b'):
        print('yes')
    elif (front[2]=='o' or back[2]=='o') and (front[1]=='b' or back[1]=='b') and (front[0]=='b' or back[0]=='b'):
        print('yes')
    else:
        print('no')