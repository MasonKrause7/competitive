def calc(time) -> str:
    global a, b, c, d, total_cycle_time_dog_1, total_cycle_time_dog_2
    dogs_attacking = 0
    
    num_full_cycles_dog_1 = time // total_cycle_time_dog_1
    minutes_into_current_cycle_1 = time % total_cycle_time_dog_1
    if minutes_into_current_cycle_1 <= a and minutes_into_current_cycle_1 != 0:
        dogs_attacking += 1
    num_full_cycles_dog_2 = time // total_cycle_time_dog_2
    minutes_into_current_cycle_2 = time % total_cycle_time_dog_2
    if minutes_into_current_cycle_2 <= c and minutes_into_current_cycle_2 != 0:
        dogs_attacking += 1
    if dogs_attacking == 0:
        return 'none'
    elif dogs_attacking == 1:
        return 'one'
    else:
        return 'both'


a,b,c,d = [int(x) for x in input().split()]

p,m,g = [int(x) for x in input().split()]

total_cycle_time_dog_1 = a+b
total_cycle_time_dog_2 = c+d

print(calc(p))
print(calc(m))
print(calc(g))


        
        
