

while True:
    sides = [int(x) for x in input().split()]
    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0:
        break
    
    sides.sort()
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if a**2+b**2 == c**2:
        print('right')
    else:
        print('wrong')
