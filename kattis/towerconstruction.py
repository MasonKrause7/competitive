n = int(input())

blocks = [int(x) for x in input().split()]

towers = 1
base = blocks[0]
for i in range(1,n):
    if blocks[i] > blocks[i-1]:
        towers += 1

print(towers)
