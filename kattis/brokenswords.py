n = int(input())

pieces = {'t': 0,
          'l': 0}

for _ in range(n):
    sword = input()
    if sword[0] == '0':
        pieces['t'] += 1
    if sword[1] == '0':
        pieces['t'] += 1
    if sword[2] == '0':
        pieces['l'] += 1
    if sword[3] == '0':
        pieces['l'] += 1


verts = pieces['t'] // 2
horiz = pieces['l'] // 2
num_swords = min(verts,horiz)
verts = pieces['t'] - num_swords*2
horiz = pieces['l'] - num_swords*2





    

print(f"{num_swords} {verts} {horiz}")
        
