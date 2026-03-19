import heapq
import random
import time

# Grid size
ROWS, COLS = 70, 70

# Obstacle density levels
DENSITY_LEVELS = {
    "low": 0.1,
    "medium": 0.2,
    "high": 0.3
}

# Directions (4-directional movement)
DIRS = [(-1,0), (1,0), (0,-1), (0,1)]

# -----------------------------
# Generate Grid with Obstacles
# -----------------------------
def generate_grid(density):
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1  # obstacle

    return grid


# -----------------------------
# Heuristic (Manhattan distance)
# -----------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -----------------------------
# A* Algorithm
# -----------------------------
def astar(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    visited_nodes = 0

    while pq:
        _, current = heapq.heappop(pq)
        visited_nodes += 1

        if current == goal:
            break

        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if grid[nx][ny] == 1:
                    continue  # obstacle

                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f_cost, (nx, ny)))
                    parent[(nx, ny)] = current

    # Reconstruct path
    path = []
    node = goal

    if node not in parent:
        return None, visited_nodes

    while node:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, visited_nodes


# -----------------------------
# Performance Metrics
# -----------------------------
def run_simulation(density_label):
    density = DENSITY_LEVELS[density_label]

    grid = generate_grid(density)

    start = (0, 0)
    goal = (69, 69)

    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    start_time = time.time()
    path, visited = astar(grid, start, goal)
    end_time = time.time()

    if path:
        print(f"\nDensity: {density_label}")
        print(f"Path Length: {len(path)}")
        print(f"Visited Nodes: {visited}")
        print(f"Time Taken: {end_time - start_time:.5f} sec")
    else:
        print(f"\nDensity: {density_label}")
        print("No path found!")


# -----------------------------
# Run for all densities
# -----------------------------
for level in ["low", "medium", "high"]:
    run_simulation(level)