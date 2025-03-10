n,m = [int(x) for x in input().split()]
expected_val_1 = 0
expected_val_2 = 0
for i in range(1, n+1):
    expected_val_1 += i * (1/n)
for i in range(1, m+1):
    expected_val_2 += i * (1/m)

print(str(expected_val_1+expected_val_2))
    


