n = int(input())

nums = [int(x) for x in input().split()]

gis = [nums[0]]
i = 0
while i < n:
    if nums[i] > gis[-1]:
        gis.append(nums[i])
    i+=1
print(len(gis))
for dig in gis:
    print(dig, end=" ")

