from heapq import *

N,T = [int(x) for x in input().split()]
a,b,c,t0 = [int(x) for x in input().split()]

prob_times = []
heappush(prob_times, t0)
i = 1
while i < N:
    heappush(prob_times, ((a*prob_times[0] + b)%c)+1)
    i+=1

clock = 0
penalty = 0
num_probs = 0
while len(prob_times) > 0:
    clock += heappop(prob_times)
    if clock < T:
        penalty += clock
        num_probs += 1
    else:
        break

print(f"{num_probs} {penalty%1000000007}")
