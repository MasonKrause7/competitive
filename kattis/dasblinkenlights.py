p,q,s = [int(x) for x in input().split()]



slow = min(p,q)
fast = max(p,q)

l2=[fast]
current = slow
c = 2 
while current <= s and current not in l2:
    l2.append(fast*c)
    current = slow*c
    c+=1

if current in l2 and current <= s:
    print("yes")
else:
    print("no")


    
