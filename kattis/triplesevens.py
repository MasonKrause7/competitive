input()

good = True
for i in range(3):
    if '7' not in input():
        good = False
        break
if good:
    print('777')
else:
    print('0')
