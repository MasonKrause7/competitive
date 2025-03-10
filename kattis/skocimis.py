a,b,c = [int(x) for x in input().split()]


left = a
mid = b
right = c
num_moves = 0

left_diff = mid-left
right_diff = right-mid

while left_diff != 1 or right_diff != 1:
    if left_diff >= right_diff:
        placement_index = mid-1
        right = placement_index
        temp = mid
        mid = right
        right = temp
    else:
        placement_index = mid+1
        left = placement_index
        temp = mid
        mid = left
        left = temp
    num_moves += 1
    left_diff = mid-left
    right_diff = right-mid
print(num_moves)
    
