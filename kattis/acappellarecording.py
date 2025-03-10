n,d = [int(x) for x in input().split()]

pitches = []

for _ in range(n):
    pitches.append(int(input()))


pitches.sort()

i = 0
j = i+1
recordings = 0

while j < n:
    if pitches[j]-pitches[i] <= d:
        j += 1
        #print(f"extending window, i={i}, j={j}, recordings={recordings}")
    else:
        recordings += 1
        i = j
        j+=1
        #print(f"collapsing window, i={i}, j={j}, recordings={recordings}")

recordings += 1   
print(recordings)
