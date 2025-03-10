import math

h,v = [int(x) for x in input().split()]

length = h / math.sin(math.radians(v))

print(str(math.ceil(length)))
