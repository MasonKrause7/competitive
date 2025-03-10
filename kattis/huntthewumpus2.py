def gen_coords(seed):
    positions = []
    for i in range(4):
        seed = seed + seed//13 + 15
        position = str(seed)[-2:]
        while position in positions:
            seed = seed + seed//13 + 15
            position = str(seed)[-2:]
        positions.append(position)
    coordinates = []
    for position in positions:
        coordinates.append([int(position[0]), int(position[1])])
    return coordinates

def calc_man_dist(x1, y1, coordinates) -> str:
    min_dist = float("inf")
    for position in coordinates:
        x2 = position[0]
        y2 = position[1]
        dist = (abs(x1-x2))+(abs(y1-y2))
        if dist < min_dist:
            min_dist = dist
    return min_dist


s = int(input())
positions = gen_coords(s)
m = 0
allFound = False

while not allFound:
    guess = input()
    if guess:
        m += 1
        x1 = int(guess[0])
        y1 = int(guess[1])
        target = [x1, y1]
        if target in positions:
            print("You hit a wumpus!")
            positions.remove(target)
        if len(positions) == 0:
            print(f"Your score is {m} moves.")
            allFound = True
        else:
            dist = calc_man_dist(x1, y1, positions)
            print(dist)
    else:
        print(f"Your score is {m} moves.")
