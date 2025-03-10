x,y = [int(x) for x in input().split()]

if (x * 4 + y * 3) % 2 == 0:
    print("possible")
else:
    print("impossible")

