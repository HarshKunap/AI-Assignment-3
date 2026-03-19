import heapq
import random

ROWS, COLS = 50, 50
DIRS = [(-1,0), (1,0), (0,-1), (0,1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    pq = [(0, start)]
    g = {start: 0}
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 0:
                new_cost = g[current] + 1

                if (nx, ny) not in g or new_cost < g[(nx, ny)]:
                    g[(nx, ny)] = new_cost
                    f = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f, (nx, ny)))
                    parent[(nx, ny)] = current

    if goal not in parent:
        return None

    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]

    return path[::-1]


def update_environment(grid):
    # randomly add/remove obstacles (simulate dynamic world)
    for _ in range(30):
        x = random.randint(0, ROWS-1)
        y = random.randint(0, COLS-1)
        grid[x][y] = random.choice([0, 1])


def dynamic_ugv():
    grid = [[0]*COLS for _ in range(ROWS)]

    start = (0, 0)
    goal = (49, 49)

    current = start
    steps = 0

    while current != goal:
        path = astar(grid, current, goal)

        if not path:
            print("No path available!")
            return

        # move one step
        current = path[1]
        steps += 1

        # simulate dynamic obstacles
        update_environment(grid)

        # keep current & goal free
        grid[current[0]][current[1]] = 0
        grid[goal[0]][goal[1]] = 0

    print("Goal reached!")
    print("Steps taken:", steps)


dynamic_ugv()