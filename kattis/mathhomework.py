
b,c,d,l = [int(x) for x in input().split()]
groupings = []
i = j = k = 0
while i*b <= l:
    while i*b + j*c <= l:
        while i*b + j*c + k*d <= l:
            legs = i*b + j*c + k*d
            if legs == l:
                if (i,j,k) not in groupings:
                    groupings.append((i,j,k))
                    print(f"{i} {j} {k}")
            k+=1
        j+=1
        k = 0
    i+=1
    j = 0
if not groupings:
    print("impossible")



    
    
