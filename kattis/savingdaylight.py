INPUT_LINE_LIMIT = 1000

def convert_time_to_minutes(time):
    hours, minutes = [int(x) for x in time.split(":")]
    time_in_minutes = hours*60 + minutes
    return time_in_minutes

    

def calculate_time_diff(start, end):
    start_time_in_minutes = convert_time_to_minutes(start)
    end_time_in_minutes = convert_time_to_minutes(end)        
    difference = end_time_in_minutes - start_time_in_minutes
    hours = difference // 60
    minutes = difference % 60
    return hours, minutes
    

def main():
    for _ in range(INPUT_LINE_LIMIT):
        line = input()
        if not line:
            break

        month, day, year, sunrise, sunset = line.split()
        hours, minutes = calculate_time_diff(sunrise, sunset)

        print(f"{month} {day} {year} {hours} hours {minutes} minutes")

if __name__ == "__main__":
    main()
    
