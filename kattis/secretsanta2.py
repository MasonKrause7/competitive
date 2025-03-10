from math import factorial, e, comb
def solve(n):
    if n >= 10:
        return 1-(1/e)
    
    num_drawings = factorial(n)
    num_bad_drawings = 0
    for i in range(1,n+1):
        num_bad_drawings += (comb(n,i)*factorial(n-i))*((-1)**(i-1))

    return num_bad_drawings/num_drawings

n = int(input())
print(solve(n))
    
