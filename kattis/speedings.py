from heapq import heappush, heappop
n = int(input())
heap = []
dist = []
time = []
t,d = input().split()
dist.append(int(d))
time.append(int(t))
for _ in range(1,n):
    t, d = [int(x) for x in input().split()]
    speed = ( (d-dist[-1])//(t-time[-1]))*-1
    dist.append(d)
    time.append(t)
    heappush(heap,speed)

print(heappop(heap)*-1)
