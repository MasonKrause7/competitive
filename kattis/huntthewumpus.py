def gen_random(seed) -> int:
    seed = int(seed) + (int(seed)//13) + 15
    myS = str(seed)
    num = myS[-2:]
    return num

def find_manhattan_dist(x1, y1, positions):
    distances = {}
    for position in positions:
        x2 = position[0]
        y2 = position[1]
        distances.update({position: (abs(x1-int(x2)))+ (abs(y1-int(y2)))})
    min_dist = float("inf")
    for position in distances.keys():
        if distances.get(position) < min_dist:
            min_dist = distances.get(position)
    return min_dist


s = int(input())

positions = []

for i in range(4):
    s = gen_random(s)
    while s in positions:
        s = gen_random(s)
    positions.append(str(s))
print(f"positions={positions}")

allWumpusesFound = False
m = 0
while not allWumpusesFound:
    guess = input()
    m += 1
    if guess in positions:
        print("You hit a wumpus!")
        positions.remove(guess)
    x1 = guess[0]
    y1 = guess[1]
    
    find_manhattan_dist(int(x1), int(y1), positions)
    print()
    if len(positions) == 0:
            print(f"Your score is {m} moves")
            allWumpusesFound = True
    


    
    






    
