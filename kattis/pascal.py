def solve(n):
    counter = n-1
    for i in range(2, n//2+1):
        if n%i==0:
            gf = n//i
            counter = n-gf
            break;
    return counter

n = int(input())
print(solve(n))
