from math import factorial, e

def solve(n):
    if n == 1:
        return 1
    if n > 170:
        return 1-(1/e)

    f = factorial(n)

    g = 0
    for i in range(n+1):
        g += ((-1)**i)/factorial(i)
      
    d = f*g

    prob_no_hits = d/f
    prob_at_least_one_hits = 1-prob_no_hits

    return prob_at_least_one_hits

n = int(input())
print(solve(n))


