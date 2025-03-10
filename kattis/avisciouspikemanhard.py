from heapq import heappush, heappop
def solve(n,t,a,b,c,t0):
    heap = []
    heappush(heap, t0)
    times = [t0]
    cycle_length = 0
    num_cycles = 0
    remaining_cells = 0

    
    for i in range(1,n):
        next_time = ((a*times[i-1]+b)%c)+1
        heappush(heap, next_time)
    clock = 0
    penalty = 0
    num_probs = 0
    while len(heap) > 0:
        prob_time = heappop(heap)
        clock += prob_time
        if clock <= t:
            penalty += clock
            num_probs += 1
        else:
            break
    return num_probs,penalty
    '''
    
    i = 1
    while i <= c and i < n:
        next_time = ((a*times[i-1]+b)%c)+1
        if next_time in times:
            cycle_length = len(times)
            num_cycles = n // cycle_length
            remaining_cells = n % cycle_length
            break
        else:
            times.append(next_time)
            heappush(heap,(next_time,i))
            heap.append((next_time,i))
            i+=1
    clock = 0
    penalty = 0
    num_probs = 0
    while len(heap) > 0:
        prob_time,index = heappop(heap)
        for j in range(num_cycles):
            clock += prob_time
            if clock <= t:
                penalty += clock
                num_probs += 1
        if index < remaining_cells:
            clock+=prob_time
            if clock <= t:
                penalty+=clock
                num_probs += 1
    return num_probs,penalty%1000000007
    '''
N,T = [int(x) for x in input().split()]
a,b,c,t0 = [int(x) for x in input().split()]

s,p = solve(N,T,a,b,c,t0)
print(f"{s} {p}")

