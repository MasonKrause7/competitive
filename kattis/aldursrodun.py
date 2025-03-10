def gcd(a, b):
    a, b = max(a,b), min(a,b)
    while b:
        rem = a % b
        a = b
        b = rem
    return a

def dfs(curr_node, path_so_far, n):
    #print(f"checking {curr_node}, path_so_far={path_so_far}")
    #print(f"length of path is {len(path_so_far)}, n={n}")
    if len(path_so_far) == n:
        #print(f"returning {path_so_far}")
        return path_so_far
    else:
        for neighbor in adjacency[curr_node]:
            if neighbor not in path_so_far:
                #print(f"{neighbor} is not in path_so_far, so we dfs it")
                path_so_far.append(neighbor)
                path = dfs(neighbor, path_so_far, n)
                if path and len(path) == n:
                    return path
                else:
                    path_so_far.pop(-1)
                    
        
    

n = int(input())

ages = [int(x) for x in input().split()]

adjacency = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if gcd(ages[i], ages[j]) > 1:
            adjacency[i].append(j)

#print(f"adjacency={adjacency}")
found = False
for i in range(len(adjacency)):
    path = dfs(i, [i], n)
    if path:
        found = True
        for elem in path:
            print(ages[elem], end = " ")
        break
if not found:
    print("Neibb")

        
    
        

