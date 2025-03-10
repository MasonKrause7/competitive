N ,Y = [int(x) for x in input().split()]

found = set()
for _ in range(Y):
    found.add(int(input()))

for i in range(N):
    if i not in found:
        print(i)
print(f"Mario got {len(found)} of the dangerous obstacles.")
