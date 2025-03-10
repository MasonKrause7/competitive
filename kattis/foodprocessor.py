import math

s,t,n = [int(x) for x in input().split()]

blades = {}

for _ in range(n):
    m,h = [int(x) for x in input().split()]

    if m in blades.keys():
        time = blades.get(m)
        if h < time:
            blades.update({m : h})
    else:
        blades.update({m : h})


max_cut_sizes = list(blades)

max_cut_sizes.sort()
for i in range(len(max_cut_sizes)):
    







    

    
    
