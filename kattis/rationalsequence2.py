t = int(input())
for _ in range(t):
    K, f  = input().split()
    k = int(K)
    delim = f.index('/')
    p = int(f[:delim])
    q = int(f[delim+1:])

    
