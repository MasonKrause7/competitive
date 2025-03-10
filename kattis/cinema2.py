n,m = [int(x) for x in input().split()]

group_sizes = [int(x) for x in input().split()]
remaining_capacity = n
for i in range(len(group_sizes)):
    if remaining_capacity >= group_sizes[i]:
        remaining_capacity -= group_sizes[i]
    else:
        print(m-i)
        break
