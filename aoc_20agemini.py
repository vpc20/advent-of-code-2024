from collections import deque


def find_cheats(grid):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = None, None
    end_x, end_y = None, None

    # Find start and end positions
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_x, start_y = i, j
            elif grid[i][j] == 'E':
                end_x, end_y = i, j

    # Find the shortest path without cheating using BFS
    queue = deque([(start_x, start_y, 0)])
    visited = set()
    distances = {}
    while queue:
        x, y, distance = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        distances[(x, y)] = distance

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != '#':
                queue.append((new_x, new_y, distance + 1))

    # Find cheats and calculate time saved
    cheats = []
    for i in range(rows):
        for j in range(cols):
            print(i,j)
            if grid[i][j] != '#':
                queue = deque([(i, j, 0, 2)])  # 2 remaining cheat steps
                visited = set()
                while queue:
                    x, y, distance, steps_left = queue.popleft()
                    if (x, y, steps_left) in visited:
                        continue
                    visited.add((x, y, steps_left))

                    if x == end_x and y == end_y and steps_left >= 0:
                        time_saved = distances[(end_x, end_y)] - distance
                        cheats.append(time_saved)
                        break

                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < rows and 0 <= new_y < cols:
                            if steps_left > 0:
                                queue.append((new_x, new_y, distance + 1, steps_left - 1))
                            elif grid[new_x][new_y] != '#':
                                queue.append((new_x, new_y, distance + 1, steps_left))

    # Count cheats saving at least 100 picoseconds
    count = 0
    for time_saved in cheats:
        if time_saved >= 100:
            count += 1

    return count


# Read the input from a file or directly as a string
with open('aoc20data1.txt', 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]

result = find_cheats(grid)
print(result)
