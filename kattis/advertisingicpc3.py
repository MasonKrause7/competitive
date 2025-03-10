def is_island(i,j) -> bool:
    if i+1 >= n:
        return False
    if j+1 >= m:
        return False
    is_valid = False
    if (matrix[i][j+1] == 'C' or matrix[i][j+1] == '?') and (matrix[i+1][j] == 'P' or matrix[i+1][j] == '?') and (matrix[i+1][j+1] == 'C' or matrix[i+1][j+1] == '?'):
        return True
    else:
        return False
    
def count_qs_curr_island(i,j) -> int:
    num_qs = 0
    if matrix[i][j] == '?':
        num_qs += 1
    if matrix[i][j+1] == '?':
        num_qs += 1
    if matrix[i+1][j] == '?':
        num_qs += 1
    if matrix[i+1][j+1] == '?':
        num_qs += 1
    return num_qs
def get_curr_position(i,j):
    top_left = (i,j)
    top_right = (i,j+1)
    bottom_left = (i+1,j)
    bottom_right = (i+1,j+1)
    position = [top_left,top_right,bottom_left,bottom_right]
    return position


n, m = [int(x) for x in input().split()]

total_qs = 0
matrix = []
for _ in range(n):
    row = input()
    for j in range(m):
        if row[j] == '?':
            total_qs+= 1
    matrix.append(row)

#the ith island had the ith number of qs and produced the ith amnt of combinations

first_island = []

combos = 0
found_one = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'I' or matrix[i][j] == '?':
            
            if is_island(i,j):
                qs_curr_island = count_qs_curr_island(i,j)
                curr_position = get_curr_position(i,j)
                if not first_island:
                    first_island = curr_position
                    combos += 3**(total_qs-qs_curr_island)
                else:
                    if any(square in curr_position for square in first_island):
                        combos += 3**(total_qs-qs_curr_island)
print(combos)
                    

                
