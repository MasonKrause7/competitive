from heapq import *

hour_values = {'12':0,
          '1': 60,
          '2': 120,
          '3': 180,
          '4': 240,
          '5': 300,
          '6': 460,
          '7': 520,
          '8': 580,
          '9': 640,
          '10': 700,
          '11': 760}
z_values = {'a.m.':0,
            'p.m.':821}
n = int(input())

while n != 0:
        heap = []
        for _ in range(n):
            time = input()
            
            h = time[:time.index(':')]
            m = time[time.index(':')+1:time.index(' ')]
            z = time[time.index(' ')+1:]

            score = z_values[z] + hour_values[h] + int(m)
            heappush(heap,(score,time))

        while len(heap)>0:
            score,time = heappop(heap)
            print(time)
        
        print()
        n = int(input())
