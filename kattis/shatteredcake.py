total_width = int(input())

N = int(input())

total_area  = 0
for n in range(N):
    width, length = [int(x) for x in input().split()]
    total_area += width*length


print(str(total_area//total_width))
    
