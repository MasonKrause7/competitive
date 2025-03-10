
while True:
    line = input()
    if len(line) == 1:
        break
    x1, y1, x2, y2, p = [float(x) for x in line.split()]

    print((abs(x1-x2)**p + abs(y1-y2)**p)**(1/p))
