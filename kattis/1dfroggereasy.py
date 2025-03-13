n, s, m = [int(x) for x in input().split()]
squares = [int(x) for x in input().split()]


h = 0
fate = 'None'
index = s-1
visited = set([index])
val = squares[index]
if val == m:
    h = 0
    fate = 'magic'
else:
    next_index = index + val
    h+=1
    while next_index >= 0 and next_index < n and squares[next_index] != m and next_index not in visited:
        visited.add(next_index)
        h += 1
        val = squares[next_index]
        next_index += val
        

    if next_index < 0:
        fate = 'left'
    elif next_index >= n:
        fate = 'right'
    elif squares[next_index] == m:
        fate = 'magic'
    elif next_index in visited:
        fate = 'cycle'


print(fate)
print(h)
