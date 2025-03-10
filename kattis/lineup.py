n = int(input())
players = []
for i in range(n):
    players.append(input())
p = players.copy()
p2 = players.copy()
p.sort()
p2.sort(reverse=True)
if p == players:
    print("INCREASING")
elif p2 == players:
    print("DECREASING")
else:
    print("NEITHER")
