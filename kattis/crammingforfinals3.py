import math
from collections import defaultdict
def distance(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

def printMatrix(position_map):
    for row in position_map:
        print(row, end="->")
        print(position_map[row])
    print()

r,c,d,n = [int(x) for x in input().split()]

position_map = defaultdict(int) 
#printMatrix(position_map)
for _ in range(n):
    i,j = [int(x) for x in input().split()]
    
    i-=1
    j-=1
      
    position_map[(i,j)] = float("inf")
    #printMatrix(position_map)
   

    for vert in range(d+1):
        for horiz in range(d+1):
            
            if (vert== 0 and horiz== 0) or (vert==d and horiz==d):
                continue
            if i+vert < r and j+horiz < c and (distance(i,j,i+vert,j+horiz) <= d):
                position_map[(i+vert,j+horiz)] += 1
                
            if i+vert < r and (j-horiz >= 0 and horiz!=0) and (distance(i,j,i+vert,j-horiz) <= d):
                position_map[(i+vert,j-horiz)] += 1
               
            if (i-vert >= 0 and vert != 0) and j+horiz < c and (distance(i,j,i-vert,j+horiz) <= d):
                position_map[(i-vert, j+horiz)] += 1
                
            if (i-vert >= 0 and vert != 0) and (j-horiz >= 0 and horiz!= 0) and (distance(i,j,i-vert,j-horiz) <= d):
                position_map[(i-vert, j-horiz)] += 1
            


        

print(min(position_map.values()))
#printMatrix(position_map)
