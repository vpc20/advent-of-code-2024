from collections import deque


def read_maze_from_file(filename):
    """Read maze input from a text file."""
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def parse_maze(maze_str):
    """Parse the maze string into a 2D grid and find start/end positions."""
    grid = [list(line) for line in maze_str.strip().split('\n')]
    start = end = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)

    if start is None or end is None:
        print("Error: Could not find start (S) or end (E) position in maze.")
        return None, None, None

    return grid, start, end


def get_neighbors(pos, grid, allow_walls=False):
    """Get valid neighboring positions."""
    if pos is None:
        print("Error: Position is None in get_neighbors")
        return []

    try:
        i, j = pos
        rows, cols = len(grid), len(grid[0])
        neighbors = []
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                if allow_walls or grid[ni][nj] in '.SE':
                    neighbors.append((ni, nj))
        return neighbors
    except Exception as e:
        print(f"Error in get_neighbors: {e}, pos={pos}")
        return []


def shortest_path(grid, start, end):
    """Find shortest path length from start to end without cheating."""
    if start is None or end is None:
        print("Error: Invalid start or end position in shortest_path")
        return float('inf')

    queue = deque([(start, 0)])
    seen = {start}

    while queue:
        pos, dist = queue.popleft()
        if pos == end:
            return dist

        for next_pos in get_neighbors(pos, grid):
            if next_pos not in seen:
                seen.add(next_pos)
                queue.append((next_pos, dist + 1))
    return float('inf')


def find_cheating_paths(grid, start, end, base_time):
    """Find all possible cheating paths and their time savings."""
    if None in (grid, start, end):
        print("Error: Invalid input to find_cheating_paths")
        return {}

    rows = len(grid)
    cols = len(grid[0])
    cheats = {}

    # Try all possible cheat start positions
    for i in range(rows):
        for j in range(cols):
            print(i, j)
            if grid[i][j] in '.SE':
                cheat_start = (i, j)
                # Time to reach cheat start
                time_to_start = shortest_path(grid, start, cheat_start)
                if time_to_start == float('inf'):
                    continue

                # Try all possible end positions within 2 moves
                seen = {cheat_start}
                queue = deque([(cheat_start, 0)])

                while queue:
                    pos, moves = queue.popleft()
                    if moves <= 2:
                        if grid[pos[0]][pos[1]] in '.SE':
                            cheat_end = pos
                            # Time from cheat end to finish
                            time_to_finish = shortest_path(grid, cheat_end, end)
                            if time_to_finish != float('inf'):
                                total_time = time_to_start + moves + time_to_finish
                                time_saved = base_time - total_time
                                if time_saved > 0:
                                    cheats[(cheat_start, cheat_end)] = time_saved

                        if moves < 2:  # Can still move through walls
                            for next_pos in get_neighbors(pos, grid, allow_walls=True):
                                if next_pos not in seen:
                                    seen.add(next_pos)
                                    queue.append((next_pos, moves + 1))

    return cheats


def count_significant_cheats(maze_str, min_time_saved=100):
    """Count number of cheats that save at least min_time_saved picoseconds."""
    # Parse the maze
    grid, start, end = parse_maze(maze_str)

    if grid is None or start is None or end is None:
        print("Error: Failed to parse maze properly")
        return 0

    # Find base completion time
    base_time = shortest_path(grid, start, end)

    if base_time == float('inf'):
        print("Error: No valid path found from start to end")
        return 0

    # Find all possible cheats
    cheats = find_cheating_paths(grid, start, end, base_time)

    # Count cheats that save at least min_time_saved
    return sum(1 for time_saved in cheats.values() if time_saved >= min_time_saved)


def main():
    filename = 'aoc_20_data1.txt'
    maze_str = read_maze_from_file(filename)

    if maze_str is not None:
        # Print the maze for verification
        print("Loaded maze:")
        print(maze_str)
        print("\nProcessing...")

        result = count_significant_cheats(maze_str)
        if result > 0:
            print(f"Number of cheats saving ≥100 picoseconds: {result}")
        else:
            print("No valid cheats found or error occurred")


if __name__ == "__main__":
    main()

# 1426
