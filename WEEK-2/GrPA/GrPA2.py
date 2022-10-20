Employee_id_1 = int(input())
Employee_id_2 = int(input())
Employee_id_3 = int(input())
Employee_id_4 = int(input())
Employee_id_5 = int(input())
if (Employee_id_1+Employee_id_2) %2 != 0:
    print("NO")
elif (Employee_id_2+Employee_id_3) %2 != 0:
    print("NO")
elif (Employee_id_3+Employee_id_4) %2 != 0:
    print("NO")
elif (Employee_id_4+Employee_id_5) %2 != 0:
    print("NO")
elif (Employee_id_5+Employee_id_1) %2 != 0:
    print("NO")
else:
    print("YES")