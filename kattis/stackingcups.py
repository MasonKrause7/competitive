import heapq

n = int(input())
heap = []

for _ in range(n):
    line = input().split()
    try:
        diameter = int(line[0])
        color = line[1]
        heapq.heappush(heap,(diameter, color))
    except:
        radius = int(line[1])
        color = line[0]
        heapq.heappush(heap,(radius*2, color))

while len(heap) > 0:
    print(heapq.heappop(heap)[1])
