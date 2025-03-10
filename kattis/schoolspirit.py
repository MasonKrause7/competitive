n = int(input())
rates = []
scores = []
full_group_score = 0
for i in range(n):
    scores.append(int(input()))
    rates.append(4**i / 5**i)
    full_group_score += scores[i]*rates[i]

final_full_group_score = full_group_score/5

i = 0
new_scores = []
while i < n:
    new_score = 0
    passed = False
    for j in range(n):
        if passed:
            new_score += scores[j]*rates[j-1]
        else: 
            if j==i:
                passed = True
                continue
            new_score += scores[j]*rates[j]
    new_scores.append(new_score/5)
    i+=1
avg = sum(new_scores)/(n)
    

print(final_full_group_score)
print(avg)

                
