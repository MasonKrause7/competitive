h,w,n = [int(x) for x in input().split()]

i = 0
messedUp = False
bricks = [int(x) for x in input().split()]
for layer in range(1,h+1):
    perfect=False
    laid = 0
    while laid<w and i < n:
        laid += bricks[i]
        i+=1
        if laid == w:
            perfect=True
    if perfect:
        continue
    else:
        messedUp=True
        break
if messedUp:
    print('NO')
else:
    print('YES')
