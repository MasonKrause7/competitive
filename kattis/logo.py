import math
t = int(input())
for _ in range(t):
    n = int(input())
    curr_position = [0,0]
    curr_direction = 0
    for _ in range(n):
        line = input().split()
        cmd = line[0]
        measure = int(line[1])

        #print(f"cmd={cmd} measure={measure}")

        if cmd == 'lt':
            curr_direction = (curr_direction+measure) %360
        elif cmd == 'rt':
            curr_direction = (curr_direction + 360 - measure) % 360

        elif cmd == 'fd':
            curr_position[0] += measure*math.cos(math.radians(curr_direction))
            curr_position[1] += measure*math.sin(math.radians(curr_direction))

        elif cmd == 'bk':
            curr_position[0] -= measure*math.cos(math.radians(curr_direction))
            curr_position[1] -= measure*math.sin(math.radians(curr_direction))

        #print(f"curr_position={curr_position}, curr_direction={curr_direction}")

    dist = math.sqrt(curr_position[0]**2 + curr_position[1]**2)
    print(round(dist))
                
        
