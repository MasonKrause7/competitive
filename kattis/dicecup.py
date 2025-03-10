n,m = [int(x) for x in input().split()]

diff = abs(n-m)
num_results = diff+1

if n == m:
    print(n+1)
else:
    smaller = min(n, m)
    bigger = max(n, m)


    results = []
    for i in range(smaller+1, bigger+2):
        results.append(i)

    for result in results:
        print(result)
