full = [1, 1, 2, 2, 2, 8]
nums = [int(x) for x in input().split()]
diff = [str(full[i] - nums[i]) for i in range(len(full))]
print(" ".join(diff))
