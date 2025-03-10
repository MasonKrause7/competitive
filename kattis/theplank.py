n = int(input())

options = [1, 2, 4]

if n == 1:
    print(1)
if n == 2:
    print(2)
if n == 3:
    print(3)

for i in range(3, n):
    options.append(sum([options[i-1], options[i-2], options[i-3]]))
print(options[len(options)-1])
