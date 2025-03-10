import math

def distance(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

r, c, d, n = [int(x) for x in input().split()]

people = []
for _ in range(n):
    row, col = [int(x) for x in input().split()]
    people.append((row - 1, col - 1))  # Adjust to 0-based indexing

min_heard = float("inf")
for row in range(r):
    for col in range(c):
        heard_count = 0
        for person_row, person_col in people:
            if row == person_row and col == person_col:

                heard_count = float("inf")
                break
            dist = distance(col, row, person_col, person_row)
            if dist <= d:
                heard_count += 1

        min_heard = min(min_heard, heard_count)

print(min_heard)
