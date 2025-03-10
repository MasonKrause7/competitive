C = float(input())
num_lawns = int(input())
total = 0.0
for i in range(num_lawns):
    w, l = [float(x) for x in input().split()]
    sqmeters = w*l
    cost = C * sqmeters
    total += cost
print(total)
    
