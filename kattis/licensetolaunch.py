n = int(input())
best_day = 0
min_junk = float("inf")
junk = [int(x) for x in input().split()]
for i in range(n):
    if junk[i] < min_junk:
        best_day = i
        min_junk = junk[i]
print(best_day)
