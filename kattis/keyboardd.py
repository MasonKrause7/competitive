s = input()
t = input()

occ_in_s = {}
occ_in_t = {}

for i in range(len(s)):
    if s[i] in occ_in_s:
        occ_in_s[s[i]] += 1
    else:
        occ_in_s[s[i]] = 1

for i in range(len(t)):
    if t[i] in occ_in_t:
        occ_in_t[t[i]] += 1
    else:
        occ_in_t[t[i]] = 1

keys = ''
for char in occ_in_s:
    if occ_in_t[char] == 2*occ_in_s[char]:
        keys+=char
print(keys)
        
