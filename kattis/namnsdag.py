name = input()
num_days = int(input())

for i in range(num_days):
    name_this_day = input()
    if len(name) != len(name_this_day):
        continue

    dif_chars = 0
    is_eligible = True
    for j in range(len(name)):
        if name[j] != name_this_day[j]:
            dif_chars += 1
            if dif_chars > 1:
                is_eligible = False
                break
    if is_eligible:
        print(i+1)
        break
        
