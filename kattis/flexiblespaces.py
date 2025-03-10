w, p = [int(x) for x in input().split()]
locations = [int(x) for x in input().split()]

for i in range(1, w+1):
    if i in locations or w-i in locations or i == w:
        print(i, end=" ")
    else:
        found = False
        for j in range(len(locations)):
            for k in range(len(locations)):
                if abs(locations[j]-locations[k]) == i:
                    print(i, end=" ")
                    found = True
                    break
            if found:
                break
            
            
                    
    
