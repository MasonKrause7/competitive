N = int(input())

count = 0
last_answer = ""
for i in range(N):
    correct_answer = input()
    if correct_answer == last_answer:
        count += 1
    last_answer = correct_answer

print(count)
    
