vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

count = 0
for c in input():
    if c in vowels:
        count += 1

print(count)
