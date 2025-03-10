y = int(input())

start = 2018*12+3
y_start = y*12


found = False

for i in range(y_start, y_start+13):
    if (i - start) % 26 == 0:
        print('yes')
        found=True
        break

if not found:
    print('no')
    


