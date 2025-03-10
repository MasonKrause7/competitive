r,c = [int(x) for x in input().split()]

print((r*(r-1)**(c-1))%998244353)
