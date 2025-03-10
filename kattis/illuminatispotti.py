
n = int(input())

neighbors = {}

for i in range(n):
    flights = [int(x) for x in input().split()]
    neighbors[i] = []
    for j in range(len(flights)):
        if flights[j] == 1:
            neighbors[i].append(j)



            
    
