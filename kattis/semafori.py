num_lights,length_of_road = [int(x) for x in input().split()]
lights = []
for _ in range(num_lights):
    lights.append([int(x) for x in input().split()])
    lights[-1].append(lights[-1][1]+lights[-1][2])

total_time = lights[0][0]
time_into_cycle = total_time % lights[0][3]
if time_into_cycle < lights[0][1]:
    total_time += lights[0][1]-time_into_cycle
for i in range(1, len(lights)):
    distance_traveled = lights[i][0]-lights[i-1][0]
    total_time += distance_traveled
    time_into_cycle = total_time % lights[i][3]
    if time_into_cycle < lights[i][1]:
        total_time += lights[i][1]-time_into_cycle

total_time += length_of_road - lights[-1][0]
print(total_time)
    
