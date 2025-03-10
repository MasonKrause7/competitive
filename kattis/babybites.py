n = int(input())
words = input().split()
good = True
for i in range(1, n+1):

    if words[i-1] == f"{i}" or words[i-1]=="mumble":
        continue
    print("something is fishy")
    good = False
    break
if good:
    print("makes sense")
