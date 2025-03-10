import heapq

n = int(input())

for i in range(n):
    s = int(input())
    segments = input().split()

    blues = []
    reds = []

    for segment in segments:
        if segment[-1] == 'B':
            heapq.heappush(blues, int(segment[:-1])*-1)
        elif segment[-1] == 'R':
            heapq.heappush(reds, int(segment[:-1])*-1)
        else:
            print('ERROR reading color')

    total_length = 0
    if len(blues) != 0 and len(reds) != 0:
        number_of_segments_each_color = min(len(blues), len(reds))
        for j in range(number_of_segments_each_color):
            total_length += heapq.heappop(blues)*-1
            total_length += heapq.heappop(reds)*-1
        total_length -= number_of_segments_each_color * 2
        print(f"Case #{i+1}: {total_length}")
        
    else:
        print(f"Case #{i+1}: 0")
    
    
    
