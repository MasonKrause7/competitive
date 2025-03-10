n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

greatest = nums[n-1]

found_one = False
for i in range(1,greatest):
    if i not in nums:
        print(i)
        found_one = True

if not found_one:
    print('good job')
