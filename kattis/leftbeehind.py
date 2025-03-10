while True:
    x,y = [int(x) for x in input().split()]
    if x == 0 and y == 0:
        break
    else:
        if x + y == 13:
            print("Never speak again.")
        elif x == y:
            print("Undecided.")
        elif x > y:
            print("To the convention.")
        else:
            print("Left beehind.")
