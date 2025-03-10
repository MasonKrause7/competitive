from collections import defaultdict

# Read the number of students
n = int(input())

# Create a dictionary to store the combinations of courses
combinations = defaultdict(int)

max_popularity = 0
# Read the courses for each student
for _ in range(n):
    # Read the courses for this student
    courses = tuple(sorted(map(int, input().split())))

    # Increment the count for this combination
    combinations[courses] += 1
    max_popularity = max(max_popularity, combinations[courses])

# Find the combination with the highest frequency
result = 0
for key in combinations.keys():
    if combinations[key] == max_popularity:
        result += combinations[key]

# Print the number of students taking the most popular combination
print(result)
