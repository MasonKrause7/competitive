n = int(input())

yours = input()
his = input()
qs = len(yours)
diffs = 0
for i in range(qs):
    if yours[i] != his[i]:
        diffs += 1
sames = qs-diffs
total = 0
def_wrong = 0
if sames <= n:
    
    total += sames
    def_wrong += n-sames
    total += qs-sames-def_wrong
else:
    total += n
    total+=diffs


print(total)
    
