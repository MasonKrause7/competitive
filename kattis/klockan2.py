import math

def degrees_to_time(degree):
    hour = int(math.floor(degree / 30))
    minute = int(round((degree - hour * 30) * 60 / 360))

    return f"{hour:02d}:{minute:02d}"

degree = float(input("Enter the angle between the hour hand and the minute hand in degrees: "))

time = degrees_to_time(degree)

print(f"The time is {time}")
