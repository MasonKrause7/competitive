import math
import sys
import heapq

s,t,n = [int(x) for x in input().split()]

blades = []
time = 0
for _ in range(n):
    blade = zip(input().split())
    blades.append(blade)
while s > t:
    use_heap = []
    notuse_heap = []
    for i in range(n):
        if blades[i][0] >= s:
            heappush(use_heap, (blades[i][1], blades[i][0]))
        elif blades[i][1] < :
            heappush(notuse_heap, blades[i][1], blades[i],[0])
    if not use_heap:
        print(-1)
        sys.exit(0)
    
    using_m, using_h = heappop(use_heap)
    next_m, next_h = heappop(notuse_heap)
    time += math.log2((using[1]/next_blade[1]))*using[0]

    s = next_blade[1]



    

    

    
    
