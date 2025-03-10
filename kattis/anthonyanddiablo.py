from math import pi
a, n = [float(x) for x in input().split()]

r = n / (2*pi)
A = pi * r**2

if A >= a:
    print("Diablo is happy!")
else:
    print("Need more materials!")
