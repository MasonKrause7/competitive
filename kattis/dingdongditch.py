def min_cost(num_projects, num_workers, costs, worker_counts):
    total_cost = 0
    for worker in range(num_workers):
        for _ in range(worker_counts[worker]):
            min_cost = float('inf')
            for project in range(num_projects):
                if costs[project] < min_cost:
                    min_cost = costs[project]
            total_cost += min_cost
            for project in range(num_projects):
                if costs[project] == min_cost:
                    costs[project] = float('inf')
    return total_cost

# Read input
input_1 = input().split()
N = int(input_1[0])
Q = int(input_1[1])

input_2 = input().split()
costs = [int(x) for x in input_2]

input_3 = input().split()
worker_counts = [int(x) for x in input_3]

# Call the function
result = min_cost(N, Q, costs, worker_counts)

# Print the result
print(result)
