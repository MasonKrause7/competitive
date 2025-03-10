vals = {"a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26}
s1 = input()
s2 = input()

sol = ""
i = j = 0
while i < len(s1) or j < len(s2):
    if i == len(s1):
        sol += s2[j]
        j+=1
        continue
    elif j == len(s2):
        sol += s1[i]
        i+=1
        continue
    
    if vals[s1[i]] <= vals[s2[j]]:
        sol += s1[i]
        i+=1
    else:
        sol += s2[j]
        j+=1
print(sol)
