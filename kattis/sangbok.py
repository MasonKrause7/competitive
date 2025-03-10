t, n = [int(x) for x in input().split()]

t = t*60
s = [int(x) for x in input().split()]
s.sort()

clock = 0
i = 0
while clock < t and i < n:
    clock += s[i]
    i+=1
if clock > t:
    clock -= s[i-1]
print(clock)
