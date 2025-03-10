


r,c,d,n = [int(x) for x in input().split()]

positions = []
for _ in range(n):
    positions.append(tuple([int(x) for x in input().split()]))

neighbors = {}

for position in positions:
    if position in neighbors:
        
            
