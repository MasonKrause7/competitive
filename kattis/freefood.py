n = int(input())
events = []
for i in range(n):
    events.append([int(x) for x in input().split()])

days = 0
i = 1
while i <= 365:
    for event in events:
        if i >= event[0] and i <= event[1]:
            days += 1
            break
    i += 1
print(days)
    
    
