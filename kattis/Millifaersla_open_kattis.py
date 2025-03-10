services = ["Monnei", "Fjee", "Dolladollabilljoll"]
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    print(services[0])
elif b < a and b < c:
    print(services[1])
elif c < a and c < b:
    print(services[2])
elif a == b and a < c:
    print(services[0])
elif a == c and a < b:
    print(services[0])
else:
    print(services[1])
    
