alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
d = []
for i in range(n):
    s = input().lower()
    d.append(s)
missing = []

for s in d:
    miss_in_s = []
    for char in alphabet:
        if char not in s:
            miss_in_s.append(char)
    missing.append(miss_in_s)
for i in range(len(missing)):
    missing[i].sort()
    if len(missing[i]) == 0:
        print("pangram")
    else:
        print('missing',end=' ')
        for miss in missing[i]:
            print(miss, end='')
        print()
    
