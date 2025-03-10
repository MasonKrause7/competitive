import math

def process_directions(start_x, start_y, start_angle, directions,n):
    """Calculates the final position and updates running totals."""
    global total_x, total_y, max_distance, avg_x, avg_y 

    x, y = start_x, start_y
    angle = start_angle

    for command, value in zip(directions[::2], directions[1::2]):
        if command == "walk":
            distance = float(value)
            x += distance * math.cos(math.radians(angle))
            y += distance * math.sin(math.radians(angle))
        elif command == "turn":
            turn_angle = float(value)
            angle = (angle + turn_angle) % 360  # Normalize angle to [0, 360)

    total_x += x
    total_y += y
    distance_from_avg = math.sqrt((x - avg_x) ** 2 + (y - avg_y) ** 2)
    max_distance = max(max_distance, distance_from_avg)
    avg_x = total_x / n
    avg_y = total_y / n

    return x, y

def main():
    global total_x, total_y, max_distance, avg_x, avg_y

    while True:
        n = int(input())
        if n == 0:
            break

        total_x, total_y = 0, 0
        max_distance = 0
        avg_x = 0
        avg_y = 0

        for _ in range(n):
            x, y, _, start, *directions = input().split()
            x, y, start_angle = float(x), float(y), float(start)
            preprocessed_directions = directions
            end_x, end_y = process_directions(x, y, start_angle, preprocessed_directions,n)
            # Update average based on latest changes

        print(f"{avg_x:.5f} {avg_y:.5f} {max_distance:.5f}")
     

if __name__ == "__main__":
    main()
