c = int(input())

for _ in range(c):
    line = [int(x) for x in input().split()]
    n = line[0]
    line = line[1:]
    avg = sum(line) / n
    num_students_above = 0
    for student in line:
        if student > avg:
            num_students_above += 1
    ratio = num_students_above/n
    percentage = ratio*100
    print(f"{percentage: .3f}%")
