x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
x3, y3 = [int(x) for x in input().split()]

positions = [(x1,y1),(x2,y2),(x3,y3)]

rise1to2 = y2-y1
rise1to3 = y3-y1
rise2to3 = y3-y2
rises = [rise1to2, rise1to3, rise2to3]

print(f"rises = {rises}")
run1to2 = x2-x1
run1to3 = x3-x1
run2to3 = x3-x2
runs = [run1to2, run1to3, run2to3]
print(f"runs = {runs}")
corner = None
foundCorner = False
for i in range(len(rises)):
    for j in range(len(runs)):
        if j == i:
            continue
        print(f"comparing abs(rises[{i}]) to abs(runs[{j}]) or {abs(rises[i])} to {abs(runs[j])}")
        if abs(rises[i]) == abs(runs[j]):
            foundCorner = True
            if i == 0 and j == 1:
                corner_index = 0
                print(f"legs are 1->2 and 1->3, corner_index=0, corner={positions[corner_index]}")
                corner = positions[corner_index]
                break
            elif i == 0 and j == 2:
                corner_index = 1
                print(f"legs are 1->2 and 2->3, corner_index=1, corner={positions[corner_index]}")
                corner = positions[corner_index]
                break
            elif i ==1 and j ==2:
                corner_index = 2
                print(f"legs are 1->3 and 2->3, corner_index=2, corner={positions[corner_index]}")
                corner = positions[corner_index]
                break
            
    if foundCorner:
        break

rise = runs[corner_index]
print(f"found rise as {rise} from runs[{corner_index}]")
run = rises[corner_index]
print(f"found run as {run} from rises[{corner_index}]")
target_y = corner[1] - rise
target_x = corner[0] - run
print("answer", target_x, target_y)
