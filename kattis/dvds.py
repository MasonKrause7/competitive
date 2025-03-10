from heapq import *
k = int(input())

for _ in range(k):
    n = int(input())
    stack = [int(x) for x in input().split()]

    dvd = 1
    for i in range(n):
        
        if stack[i] == dvd:
            continue
        else:
            
