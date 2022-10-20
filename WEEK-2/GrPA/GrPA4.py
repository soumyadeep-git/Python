name1 = input()
dob1 = input()

name2 = input()
dob2 = input()

if (int(dob1[6 : 10]) == int(dob2[6 : 10])):
    if (int(dob1[3 : 5]) == int(dob2[3 : 5])):
        if (int(dob1[0 : 2]) == int(dob2[0 : 2])):
            if (name1 < name2):
                print(name1)
            else:
                print(name2)
        elif (int(dob1[0 : 2]) > int(dob2[0 : 2])):
            print(name1)
        else:
            print(name2)
    elif (int(dob1[3 : 5]) > int(dob2[3 : 5])):
        print(name1)
    else:
        print(name2)
elif (int(dob1[6 : 10]) > int(dob2[6 : 10])):
    print(name1)
else:
    print(name2)