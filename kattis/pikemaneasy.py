N,T = [int(x) for x in input().split()]
a,b,c,t0 = [int(x) for x in input().split()]

prob_times = [t0]
i = 1
while i < N:
    prob_times.append(((a*prob_times[i-1] + b)%c)+1)
    i+=1
prob_times.sort()

clock = 0
penalty = 0
num_probs = 0
for t in range(len(prob_times)):
    clock += prob_times[t]
    if clock < T:
        penalty += clock
        num_probs += 1
    else:
        break

print(f"{num_probs} {penalty%1000000007}")
