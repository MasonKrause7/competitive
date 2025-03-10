def findCritPoint(a,b):
    if b == 0:
        return 0
    return (-1)*b/(2*a)
n = int(input())
people = []
maxTemp = 0
critPoints = []
sum_a = 0
sum_b = 0
sum_c = 0
for _ in range(n):
    a,b,c,t = [int(x) for x in input().split()]
    people.append([t,a,b,c])
people.sort(reverse=True)
for i in range(n):
    t,a,b,c = people[i]
    sum_a += a
    sum_b += b
    sum_c += c
    if a < 0:
        critPoints.append(findCritPoint(a,b))
    if sum_a < 0:
        critPoints.append(findCritPoint(sum_a, sum_b))
        #print(f"new crit point of the ag = {critPoints[-1]}")
    if t > maxTemp:
        maxTemp = t
critPoints.sort()
x = 0
c = 0
p = len(people)-1
maxHappiness = 0
while x <= maxTemp:
    #print(f"x={x}, c={c}, p={p}, sum_a={sum_a}, sum_b={sum_b}, sum_c={sum_c}")
    while p < len(people) and x > people[p][0]:
        sum_a -= people[p][1]
        sum_b -= people[p][2]
        sum_c -= people[p][3]
        #print(f"removed person {p}, whose maxTemp={people[p][0]}, sum_a={sum_a}, sum_b={sum_b}, sum_c={sum_c}")
        p-=1
    happiness = sum_a*x**2 + sum_b*x + sum_c
    #print(f"happiness from {sum_a}*{x}**2+{sum_b}*{x}+{sum_c} = {happiness}, maxHappiness={maxHappiness}")
    maxHappiness = max(maxHappiness, happiness)     
    if c < len(critPoints) and critPoints[c] < x+1:
        #evaluate agg function at critPoint
        #print(f"found critPoint {critPoints[c]} < x+1, evaluating at crit point")
        happiness = sum_a*critPoints[c]**2 + sum_b*critPoints[c] + sum_c
        #print(f"happiness found={happiness}")
        maxHappiness = max(maxHappiness, happiness)
        c+=1 
    x+=1
print(float(maxHappiness))
    

    




    
