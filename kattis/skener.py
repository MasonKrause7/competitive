r, c, zr, zc = [int(x) for x in input().split()]

result = [[]]
for i in range(r):
    row = input()
    for e in range(zr):
        for j in range(c):
            char = row[j]
            for f in range(zc):
                print(char, end="")
        print()
