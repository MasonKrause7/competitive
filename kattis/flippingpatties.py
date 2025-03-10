n = int(input())

d = {}
for i in range(n):
    b,t = [int(x) for x in input().split()]

    time_of_flip = t-b
    time_put_on = t-(2*b)
    time_pulled_off = t
    
    if time_of_flip in d:
        d[time_of_flip] += 1
    else:
        d[time_of_flip] = 1

    if time_put_on in d:
        d[time_put_on] += 1
    else:
        d[time_put_on] = 1

    if time_pulled_off in d:
        d[time_pulled_off] += 1
    else:
        d[time_pulled_off] = 1


most_ops = max(d.values())
most_cooks = most_ops//2 + most_ops % 2
print(most_cooks)
