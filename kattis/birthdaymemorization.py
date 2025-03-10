N = int(input())

birthday_to_priority = {}
for n in range(N):
    name, priority, birthday = [x for x in input().split()]

    if birthday in birthday_to_priority.keys():
        if birthday_to_priority.get(birthday)[0] < int(priority):
            birthday_to_priority.update({birthday: [int(priority), name]})
        elif birthday_to_priority.get(birthday)[0] > int(priority):
            pass
    else:
        birthday_to_priority.update({birthday: [int(priority), name]})
            

keys = birthday_to_priority.keys()
print(len(keys))
names = []

for key in keys:
    names.append(birthday_to_priority.get(key)[1])

names.sort()
for name in names:
    print(name)

    
