def winningX(a,b,c,t):
    x = 0
    if a == 0:
        x = 0
    else:
        x = ((-1)*b)/(2*a)
    val0 = a*0**2 +b*0+c
    valt = a*t**2+b*t+c
    valx = a*x**2+b*x+c

    if val0 >= valt and val0 >= valx:
        return 0
    elif valt >= val0 and valt >= valx:
        return t
    else:
        return x

def findX(a,b,c,t):
    x = 0
    if a == 0:
        x = 0
    else:
        x = ((-1)*b)/(2*a)
    return x
n = int(input())
people = []
for _ in range(n):
    people.append([int(x) for x in input().split()])

maxHap = 0
idealX = 0
for i in range(len(people)):
    #x = winningX(people[i][0], people[i][1], people[i][2], people[i][3])
    a,b,c,t = people[i]
    x = findX(a, b, c, t)
    hap0 = a*0**2 + b*0 + c
    hapx = a*x**2 + b*x + c
    hapt = a*t**2 + b*t + c
    for j in range(len(people)):
        if i == j:
            continue
        if people[j][3] >= x:
            hapx += people[j][0]*x**2 + people[j][1]*x + people[j][2]
        if people[j][3] >= t:
            hapt += people[j][0]*t**2 + people[j][1]*t + people[j][2]
        hap0 += people[j][0]*0**2 + people[j][1]*0 + people[j][2]    
            
    
    maxHap = max(maxHap, hapx, hapt, hap0)

print(float(maxHap))
