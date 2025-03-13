total_weight, num_stacks = [int(x) for x in input().split()]

t_weight = 29260
g_weight = 29370
total_coins = (num_stacks*(num_stacks+1))/2


for i in range(1, num_stacks+1):
    remaining_coins = total_coins - i

    weight_this_stack = i * g_weight

    remaining_weight = total_weight - weight_this_stack

    if remaining_weight == remaining_coins*t_weight:
        print(i)
        break
    
    
    
