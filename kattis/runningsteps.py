from math import factorial
def solve(s):
    qual_coefs = []
    for i in range(s):
        for j in range(i+1):
            if i*4 + j*2 == n:
                qual_coefs.append([i,j])
    
    

t = int(input())

for _ in range(t):
    k,s = [int(x) for x in input().split()]

    
