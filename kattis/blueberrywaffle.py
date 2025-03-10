r, f = [int(x) for x in input().split()]

num_180s = f/r


total_degrees = 180 * num_180s

remaining_turn = total_degrees%360

if remaining_turn > 90 and remaining_turn < 270:
    print("down")
else:
    print("up")
