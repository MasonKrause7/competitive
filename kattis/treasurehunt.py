r, c = [int(x) for x in input().split()]
grid = []
for i in range(r):
    grid.append(input())
    
current_position = (0,0)
moves = 0
visited = set()
directions = {'N':(-1,0),'S':(1,0),'E':(0,1),'W':(0,-1)}

while current_position[0] >= 0 and current_position[0] < r and current_position[1] >= 0 and current_position[1] < c:
    i, j = current_position
    if grid[i][j] == 'T':
        print(moves)
        break
    i_dir, j_dir = directions.get(grid[i][j])
    i += i_dir
    j += j_dir
    next_position = (i,j)
    if next_position in visited:
        print('Lost')
        break
    else:
        visited.add(next_position)
        current_position = next_position
        moves += 1
    


if current_position[0] < 0 or current_position[0] >= r or current_position[1] < 0 or current_position[1] >= c:
    print('Out')
