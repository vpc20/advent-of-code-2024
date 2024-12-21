from collections import deque
from functools import lru_cache


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
    # Using list comprehension for faster parsing
    grid = [list(line) for line in maze_str.strip().split('\n')]

    # Pre-calculate dimensions
    rows, cols = len(grid), len(grid[0])

    # Create a set of valid positions for faster lookup
    valid_positions = set()
    start = end = None

    # Single pass through the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in '.SE':
                valid_positions.add((i, j))
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)

    if start is None or end is None:
        return None, None, None, None

    return grid, start, end, valid_positions


# Cache the neighbors calculation for repeated positions
@lru_cache(maxsize=1024)
def get_cached_neighbors(pos, rows, cols):
    """Get potential neighboring positions."""
    i, j = pos
    neighbors = []
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            neighbors.append((ni, nj))
    return neighbors


def get_neighbors(pos, grid, valid_positions, allow_walls=False):
    """Get valid neighboring positions using cached results."""
    if pos is None:
        return []

    neighbors = get_cached_neighbors(pos, len(grid), len(grid[0]))
    if allow_walls:
        return neighbors
    return [n for n in neighbors if n in valid_positions]


def shortest_path(grid, start, end, valid_positions):
    """Find shortest path length using bidirectional BFS."""
    if start is None or end is None:
        return float('inf')

    # Bidirectional BFS
    start_queue = deque([(start, 0)])
    end_queue = deque([(end, 0)])
    start_seen = {start: 0}
    end_seen = {end: 0}

    while start_queue and end_queue:
        # Expand from start
        pos, dist = start_queue.popleft()
        if pos in end_seen:
            return dist + end_seen[pos]

        for next_pos in get_neighbors(pos, grid, valid_positions):
            if next_pos not in start_seen:
                start_seen[next_pos] = dist + 1
                start_queue.append((next_pos, dist + 1))

        # Expand from end
        pos, dist = end_queue.popleft()
        if pos in start_seen:
            return dist + start_seen[pos]

        for next_pos in get_neighbors(pos, grid, valid_positions):
            if next_pos not in end_seen:
                end_seen[next_pos] = dist + 1
                end_queue.append((next_pos, dist + 1))

    return float('inf')


def find_cheating_paths(grid, start, end, base_time, valid_positions):
    """Find all possible cheating paths using optimized search."""
    if None in (grid, start, end):
        return {}

    rows, cols = len(grid), len(grid[0])
    cheats = {}

    # Use valid_positions set instead of checking grid directly
    for cheat_start in valid_positions:
        print(cheat_start)
        time_to_start = shortest_path(grid, start, cheat_start, valid_positions)
        if time_to_start == float('inf'):
            continue

        # BFS for cheat end positions
        seen = {cheat_start}
        queue = deque([(cheat_start, 0)])

        while queue:
            pos, moves = queue.popleft()
            if moves <= 2:
                if pos in valid_positions:
                    cheat_end = pos
                    time_to_finish = shortest_path(grid, cheat_end, end, valid_positions)
                    if time_to_finish != float('inf'):
                        total_time = time_to_start + moves + time_to_finish
                        time_saved = base_time - total_time
                        if time_saved > 0:
                            cheats[(cheat_start, cheat_end)] = time_saved

                if moves < 2:
                    for next_pos in get_neighbors(pos, grid, valid_positions, allow_walls=True):
                        if next_pos not in seen:
                            seen.add(next_pos)
                            queue.append((next_pos, moves + 1))

    return cheats


def count_significant_cheats(maze_str, min_time_saved=100):
    """Count number of cheats that save at least min_time_saved picoseconds."""
    grid, start, end, valid_positions = parse_maze(maze_str)

    if grid is None:
        return 0

    base_time = shortest_path(grid, start, end, valid_positions)
    if base_time == float('inf'):
        return 0

    cheats = find_cheating_paths(grid, start, end, base_time, valid_positions)
    return sum(1 for time_saved in cheats.values() if time_saved >= min_time_saved)


def main():
    filename = 'aoc20data1.txt'
    maze_str = read_maze_from_file(filename)

    if maze_str is not None:
        result = count_significant_cheats(maze_str)
        print(f"Number of cheats saving ≥100 picoseconds: {result}")


if __name__ == "__main__":
    main()