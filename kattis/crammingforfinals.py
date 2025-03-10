import math

class Node:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.points = []
        self.children = []

    def contains(self, x, y):
        return self.x0 <= x <= self.x1 and self.y0 <= y <= self.y1

    def subdivide(self):
        mid_x = (self.x0 + self.x1) / 2
        mid_y = (self.y0 + self.y1) / 2
        self.children = [
            Node(self.x0, self.y0, mid_x, mid_y),
            Node(mid_x, self.y0, self.x1, mid_y),
            Node(self.x0, mid_y, mid_x, self.y1),
            Node(mid_x, mid_y, self.x1, self.y1)
        ]

    def insert(self, x, y):
        if not self.contains(x, y):
            return False
        if len(self.points) < 4 and not self.children:  # Adjust capacity as needed
            self.points.append((x, y))
            return True
        if not self.children:
            self.subdivide()
        for child in self.children:
            if child.insert(x, y):
                return True
        return False

    def range_query(self, x, y, radius):
        points_in_range = []
        if not self:
            return points_in_range
        if math.sqrt((self.x0 - x)**2 + (self.y0 - y)**2) <= radius or \
           math.sqrt((self.x1 - x)**2 + (self.y1 - y)**2) <= radius or \
           math.sqrt((self.x0 - x)**2 + (self.y1 - y)**2) <= radius or \
           math.sqrt((self.x1 - x)**2 + (self.y0 - y)**2) <= radius:
            for px, py in self.points:
                if math.sqrt((px - x)**2 + (py - y)**2) <= radius:
                    points_in_range.append((px, py))
            if self.children:
                for child in self.children:
                    points_in_range.extend(child.range_query(x, y, radius))
        return points_in_range


def min_hearing_distance(grid_size, occupied_points, hearing_distance):
    """
    Calculates the minimum number of people you could hear in a grid.

    Args:
      grid_size: A tuple (m, n) representing the grid dimensions.
      occupied_points: A list of tuples (i, j) representing occupied grid points.
      hearing_distance: The Euclidean distance at which you can hear someone.

    Returns:
      The minimum number of people you could hear.
    """
    m, n = grid_size
    quadtree = Node(0, 0, m - 1, n - 1) 

    # Insert occupied points into the quadtree
    for i, j in occupied_points:
        quadtree.insert(i, j)

    min_heard = float('inf')
    occupied_set = set(occupied_points)

    # Pre-calculate squared distances
    max_distance_squared = hearing_distance * hearing_distance 
    distance_cache = {} 

    for x in range(m):
        for y in range(n):
            if (x, y) not in occupied_set:
                heard_count = 0
                for px, py in quadtree.range_query(x, y, hearing_distance):
                    # Calculate squared distance and cache it
                    key = (abs(x - px), abs(y - py))  # Use absolute difference as key
                    if key not in distance_cache:
                        distance_cache[key] = (x - px)**2 + (y - py)**2
                    
                    if distance_cache[key] <= max_distance_squared:
                        heard_count += 1

                min_heard = min(min_heard, heard_count)
                if min_heard == 0:
                    return 0

    return min_heard

# Example usage
r,c,d,n = [int(x) for x in input().split()]
occupied = []
for _ in range(n):
    position = [int(x) for x in input().split()]
    position[0] -= 1
    position[1] -= 1
    pos = tuple(position)
    occupied.append(pos)
#print(f"occupied={occupied}")

min_heard = min_hearing_distance((r,c), occupied, d)
print(min_heard)


    
