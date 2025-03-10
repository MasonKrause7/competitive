a1, b1, a2, b2 = [int(x) for x in input().split()]
a3, b3, a4, b4 = [int(x) for x in input().split()]

num_sides_die_1 = b1 - a1 + 1
num_sides_die_2 = b2 - a2 + 1

num_sides_die_3 = b3-a3+1
num_sides_die_4 = b4-a4+1

prob_die_1 = 1/num_sides_die_1
prob_die_2 = 1/num_sides_die_2
prob_die_3 = 1/num_sides_die_3
prob_die_4 = 1/num_sides_die_4

expected_val_die_1, expected_val_die_2, expected_val_die_3, expected_val_die_4 = 0, 0, 0, 0

for i in range(a1, b1+1):
    expected_val_die_1 += prob_die_1 * i
for i in range(a2, b2+1):
    expected_val_die_2 += prob_die_2 * i
for i in range(a3, b3+1):
    expected_val_die_3 += prob_die_3 * i
for i in range(a4, b4+1):
    expected_val_die_4 += prob_die_4 * i

player1_expected_val = expected_val_die_1 + expected_val_die_2
player2_expected_val = expected_val_die_3 + expected_val_die_4

if player1_expected_val > player2_expected_val:
    print("Gunnar")
elif player2_expected_val > player1_expected_val:
    print("Emma")
else:
    print("Tie")
