while True:
    n = int(input())
    if n == 0:
        break

    l1 = []
    l2 = []
    for _ in range(n):
        l1.append(int(input()))
    for _ in range(n):
        l2.append(int(input()))

    l1_c = l1.copy()
    l1_c.sort()
    l2.sort()

    correspondings = {}
    for i in range(n):
        correspondings[l1_c[i]] = l2[i]

    for i in range(n):
        print(correspondings[l1[i]])
