nums = [int(x) for x in input().split()]

target_sum_1 = nums[6]
target_sum_2 = nums[7]
tower_1 = []
tower_2 = []
nums = nums[0:6]

found = False
for i in range(len(nums)-1):

    for j in range(i+1,len(nums)):
        compliment1 = target_sum_1-nums[i]-nums[j]
        if compliment1 in nums and compliment1 != nums[i] and compliment1 != nums[j]:
            found = True
            tower_1 = [compliment1, nums[i], nums[j]]
            #print(f"compliment1 was in nums, {compliment1}... tower1={tower_1}")
            for num in nums:
                if num not in tower_1:
                    #print(f"since {num} not in tower_1, adding {num} to tower_2")
                    tower_2.append(num)
                    #print(f"tower2 = {tower_2}")
            break
        compliment2 = target_sum_2-nums[i]-nums[j]
        if compliment2 in nums and compliment2 != nums[i] and compliment2 != nums[j]:
            found = True
            tower_2 = [compliment2, nums[i], nums[j]]
            #print(f"compliment2 was in nums, {compliment2}... tower_2 = {tower_2}")
            for num in nums:
                if num not in tower_2:
                    tower_1.append(num)
                    #print(f"since {num} not in tower_2, adding {num} to tower_1")
                    #print(f"tower1 ={tower_1}")
        if found:
            break
    if found:
        break

tower_1.sort(reverse=True)
tower_2.sort(reverse=True)
for i in range(3):
    print(tower_1[i], end=" ")
for i in range(3):
    print(tower_2[i], end=" ")
