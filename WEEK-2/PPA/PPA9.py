num_of_coins = int(input())
share_a = int(input())
share_b = int(input())
share_c = int(input())

if share_a and share_b and share_c <= 0: print("UNFAIR")
elif share_a == share_b or share_b == share_c or share_c == share_a: print("UNFAIR")
elif share_a + share_b + share_c != num_of_coins: print("UNFAIR")
else:print("FAIR")