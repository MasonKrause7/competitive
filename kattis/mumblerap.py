import re

regex = "([1-9][0-9]*)"

pattern = re.compile(regex)

input()

nums = re.findall(pattern, input())

biggestNum = 0

for num in nums:
    if int(num) > biggestNum:
        biggestNum = int(num)
print(biggestNum)
