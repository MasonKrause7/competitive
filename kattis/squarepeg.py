from math import sqrt

l,r = [int(x) for x in input().split()]


if r >= sqrt(1/2)*l:
    print('fits')
else:
    print('nope')
