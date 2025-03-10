s = input()

c= {'T': 0,
    'C': 0,
    'G': 0}
for i in range(len(s)):
    c[s[i]] += 1

print(min(c.values())*7+c['T']**2+c['C']**2+c['G']**2)
