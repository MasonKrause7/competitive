input()

nums = [int(x) for x in input().split()]

expenses = 0
for num in nums:
    if num < 0:
        expenses += num

print(abs(expenses))
