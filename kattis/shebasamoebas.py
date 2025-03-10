def build_grid(m,n):
    
    grid = []
    for i in range(m):
        line = input()
        row = []
        for c in line:
            if c == '.':
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid

def dfs(position, grid, seen):
    if position in seen:
        return
    seen.add(position)
    i,j = position
    directions = [(1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1)]
    neighboring_positions = []
    for direction in directions:
        delta_i, delta_j = direction
        if i+delta_i <= m-1 and i+delta_i >= 0 and j+delta_j<=n-1 and j+delta_j >= 0:
            if grid[i+delta_i][j+delta_j] == 1 and (i+delta_i, j+delta_j) not in seen:
                dfs((i+delta_i, j+delta_j), grid, seen)


m,n = (int(x) for x in input().split())
seen = set()
grid = build_grid(m,n)
num_loops = 0
for i in range(m):
    for j in range(n):
        if (i,j) not in seen and grid[i][j] == 1:
            dfs((i,j), grid, seen)
            num_loops += 1
print(num_loops)
            
