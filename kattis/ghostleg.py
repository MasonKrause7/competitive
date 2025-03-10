n, m = [int(x) for x in input().split()]

rungs = []
for i in range(m):
    rungs.append(int(input()))

results = {}
for i in range(1, n+1):
    curr_line = i
    for rung in rungs:
        if rung == curr_line-1: #go left
            curr_line -= 1
        elif rung == curr_line: #go right
            curr_line += 1
    results.update({curr_line: i})

for i in range(1, n+1):
    print(results.get(i))
    
