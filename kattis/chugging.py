n = int(input())
ta, da = [int(x) for x in input().split()]
tb, db = [int(x) for x in input().split()]

time_a = 0
time_b = 0
for i in range(0,n):
    time_a += da*i + ta
    time_b += db*i + tb

if time_a == time_b:
    print("=")
elif time_a < time_b:
    print("Alice")
elif time_b < time_a:
    print("Bob")
