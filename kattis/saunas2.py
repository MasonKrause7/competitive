def findX(a, b):
    if a == 0 or b == 0:
        return 0
    return (-1)*b/(2*a)

n = int(input())
people = []
maxTemp = 0
xVals = set()
checked = set()
for _ in range(n):
    people.append([int(x) for x in input().split()])
    xVals.add(findX(people[-1][0],people[-1][1]))
    if people[-1][3] > maxTemp:
        maxTemp = people[-1][3]

maxHap = 0
for x in range(maxTemp+1):
    hap = 0
    for i in range(len(people)):
        a, b, c, t = people[i]
        if t >= x:
            hap += a*x**2+b*x+c
    checked.add(x)
    maxHap = max(maxHap, hap)

for val in xVals:
    hap = 0
    if val in checked:
        continue
    for i in range(len(people)):
        a, b, c, t = people[i]
        if t >= val:
            hap += a*val**2+b*val+c
    maxHap = max(maxHap, hap)
print(float(maxHap))
