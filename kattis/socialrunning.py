n = int(input())
d = []
pairs = []
for _ in range(n):
    d.append(int(input()))

for i in range(n):
    first_dist = d[i]
    next_dist = d[(i + (2*n - 2)) % n]
    pairs.append(first_dist+next_dist)
print(min(pairs))
