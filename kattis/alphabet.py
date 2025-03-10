s = input()
n = len(s)
dp = [25] * n
dp[0] = 25
i = 1

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

while i < n:
    potentials = [25] * i
    curr_char = s[i]
    for j in range(i):
        preceding_char = s[j]
        if vals[preceding_char] < vals[curr_char]:
            potential = dp[j]-1
            potentials[j] = potential
    dp[i] = min(potentials)
    i+=1
print(min(dp))








        
    
