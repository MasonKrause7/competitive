n = int(input())
presses = [int(input()) for _ in range(n)]

time = 0
running = False
last_press = 0

for press in presses:
    if running:
        time += press - last_press
    running = not running
    last_press = press

if running:
    print("still running")
else:
    print(time)
