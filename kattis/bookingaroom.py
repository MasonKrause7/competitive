r, n = [int(x) for x in input().split()]
booked = set()
for i in range(n):
    room_num = int(input())
    booked.add(room_num)
if n >= r:
    print("too late")
else:
    for i in range(1,r+1):
        if i not in booked:
            print(i)
            break
    
