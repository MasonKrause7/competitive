e, f, c = [int(x) for x in input().split()]

total = 0
num_sodas_bought = (e+f)//c
empties_left_over = (e+f)%c
total += num_sodas_bought
empties_left_over += num_sodas_bought
num_sodas_bought = 0
while empties_left_over >= c:
    num_sodas_bought = empties_left_over//c
    left_overs = empties_left_over%c
    total += num_sodas_bought
    empties_left_over = num_sodas_bought + left_overs
    num_sodas_bought = 0
    

print(total)
