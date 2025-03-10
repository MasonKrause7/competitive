input()

nums = [int(x) for x  in input().split()]
count = 0
for num in nums:
    if num < 0:
        count+= 1

print(count)
