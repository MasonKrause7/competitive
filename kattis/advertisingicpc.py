

def check_down(i, j):
    if matrix[i+1][j] == 'P' or matrix[i+1][j] == '?':
        if matrix[i+1][j] == '?':
            if (i+1,j) in locked_as:
                locked_as.update({(i+1,j) : locked_as.get((i+1,j)).append('P')})
            else:
                locked_as.update({(i+1,j) : ['P']})
        #print(f"down from ({i},{j}) is {matrix[i+1][j]} so ({i},{j}) is still a potential island")
        return True
    else:
        return False
def check_right(i, j):
    if matrix[i][j+1] == 'C' or matrix[i][j+1] == '?':
        if matrix[i][j+1] == '?':
            if (i,j+1) in locked_as:
                locked_as.update({(i, j+1) : locked_as.get((i,j+1)).append('C')})
            else:
                locked_as.update({(i,j+1) : ['C']})
        #print(f"right from ({i},{j}) is {matrix[i][j+1]} so ({i},{j}) is still a potential island")
        return True
    else:
        return False
def check_down_right(i, j):
    if matrix[i+1][j+1] == 'C' or matrix[i+1][j+1] == '?':
        if matrix[i+1][j+1] == '?':
            if (i+1,j+1) in locked_as:
                locked_as.update({(i+1, j+1) : locked_as.get((i+1,j+1)).append('C')})
            else:
                locked_as.update({(i+1,j+1) : ['C']})
        #print(f"down_right from ({i},{j}) is {matrix[i+1][j+1]} so ({i},{j}) is still a potential island")
        return True
    else:
        return False

    
def is_island(i, j):
    #print("CALLED IS ISLAND")
    if check_down(i,j) and check_right(i,j) and check_down_right(i,j):
        return True
    else:
        return False
    
def find_num_qs_this_island(i,j):
    qs_this_island = 0
    if matrix[i][j] == '?':
        qs_this_island += 1
    if matrix[i+1][j] == '?':
        qs_this_island +=1
    if matrix[i][j+1] == '?':
        qs_this_island += 1
    if matrix[i+1][j+1] == '?':
        qs_this_island += 1
    return qs_this_island

n,m = [int(x) for x in input().split()]

matrix = []
locked_as = {}
total_qs = 0

for _ in range(n):
    row = input()
    matrix.append(row)
    for j in range(m):
        if row[j] == '?':
            total_qs += 1

permuts = []
qs_in_islands = []
island = 0

for i in range(n):
    for j in range(m):
        #print(f"at position ({i},{j})")
        if (matrix[i][j] == 'I' or matrix[i][j] == '?') and j+1 < m and i+1 < n:
            if is_island(i,j):
                #print(f"position ({i},{j}) is an island")
                qs_in_islands.append(find_num_qs_this_island(i,j))
                #print(f"qs_in_island[{island}] = {qs_in_islands[island]}")
                if not permuts:
                    permuts.append(3**(total_qs-qs_in_islands[island]))
                    #print(f"First island, num permutes is {permuts[(len(permuts)-1)]}")
                else:
                    permuts.append((3**(qs_in_islands[len(qs_in_islands)-1])-1)*permuts[len(permuts)-1])
                    #print(f"island {island}, num permutes is {permuts[(len(permuts)-1)]} ")
                island += 1

print(permuts[len(permuts)-1]%998244353)


