max_sum = 0
winner_index = 0
for i in range(5):
    points = sum([int(x) for x in input().split()])
    if points > max_sum:
        max_sum = points
        winner_index = i+1
    else:
        pass

print(winner_index, max_sum)
