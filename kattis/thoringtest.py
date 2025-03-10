n = int(input())
words = set()

for _ in range(n):
    words.add(input().lower())

contains_error = False
sentence = input().split()
for word in sentence:
    if word.lower() not in words:
        print("Thore has left the chat")
        contains_error = True
        break

if not contains_error:
    print("Hi, how do I look today?")
