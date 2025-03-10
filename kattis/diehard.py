a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

a_wins_v_b = 0
a_ties_v_b = 0
a_wins_v_c = 0
a_ties_v_c = 0
b_wins_v_a = 0
b_wins_v_c = 0
b_ties_v_a = 0
b_ties_v_c = 0
c_wins_v_a = 0
c_wins_v_b = 0
c_ties_v_a = 0
c_ties_v_b = 0

for i in range(6):
    for j in range(6):
        if a[i] > b[j]:
            a_wins_v_b += 1
        elif a[i] == b[j]:
            a_ties_v_b += 1
            b_ties_v_a += 1
        else:
            b_wins_v_a += 1

        if a[i] > c[j]:
            a_wins_v_c += 1
        elif a[i] == c[j]:
            a_ties_v_c += 1
            c_ties_v_a += 1
        else:
            c_wins_v_a += 1

        if b[i] > c[j]:
            b_wins_v_c += 1
        elif b[i] == c[j]:
            b_ties_v_c += 1
            c_ties_v_b += 1
        else:
            c_wins_v_b += 1

if (a_ties_v_c != 36 and a_ties_v_b != 36) and a_wins_v_b /((6*6)-a_ties_v_b) >= .5 and a_wins_v_c / ((6*6)-a_ties_v_c) >= .5:
    print(1)
elif (b_ties_v_a != 36 and b_ties_v_c != 36) and b_wins_v_a /((6*6)-b_ties_v_a) >= .5 and b_wins_v_c / ((6*6)-b_ties_v_c) >= .5:
    print(2)
elif (c_ties_v_a != 36 and c_ties_v_b != 36) and c_wins_v_a /((6*6)-c_ties_v_a) >= .5 and c_wins_v_b / ((6*6)-c_ties_v_b) >= .5:
    print(3)
else:
    print("No dice")
            
        

