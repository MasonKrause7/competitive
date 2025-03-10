from heapq import heappush, heappop
n = int(input())

times = [int(x) for x in input().split()]
times.sort()
#print(times)
day = 1
party = 1
while n-day >= 0:
    time = times[n-day]
    #print(f"day={day}, n-day={n-day}, time={time}, time+day={time+day}, party={party}")
    if time + day > party:
        party = time + day
    day += 1
print(party+1)
    
        
