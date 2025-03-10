results = []
n = int(input())
for i in range(n):
    row = [int(x) for x in input().split()]
    for j in range(n):
        if row[j] > 0:
            result = [i+1, j+1, row[j]]
            results.append(result)

print(len(results))
for result in results:
    print(f"{result[0]} {result[1]} {result[2]}")
