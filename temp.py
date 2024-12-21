from collections import deque
from typing import List, Tuple, Optional


def bfs_grid(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Performs BFS on a grid to find shortest path from start to end.

    Args:
        grid: 2D list where 0 represents walkable path and 1 represents walls
        start: Starting coordinates (row, col)
        end: Target coordinates (row, col)

    Returns:
        List of coordinates representing the path from start to end,
        or None if no path exists
    """
    if not grid or not grid[0]:
        return None

    nrows, ncols = len(grid), len(grid[0])

    # Queue for BFS
    q = deque([(start, [start])])
    visited = {start}
    # path = [start]

    while q:
        coord, path = q.popleft()
        r, c = coord
        if (r, c) == end:
            return path

        # Try all possible directions
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
            # Check if the next position is valid and unvisited
            if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] != 1 and (nr, nc) not in visited:
                # if (nr, nc) == end:
                #     return path + [(nr, nc)]
                q.append(((nr, nc), path + [(nr, nc)]))
                visited.add((nr, nc))

    return None


def print_path_in_maze(maze: List[List[int]], path: List[Tuple[int, int]]):
    """Visualize the path in the maze"""
    # Create a copy of the maze for visualization
    vis_maze = [row[:] for row in maze]

    # Mark the path with '*'
    for row, col in path:
        vis_maze[row][col] = '*'

    # Print the maze with the path
    for row in vis_maze:
        print(' '.join(['*' if cell == '*' else '#' if cell == 1 else '.' for cell in row]))


# Example usage with visualization
if __name__ == "__main__":
    # 0 represents path, 1 represents wall
    # maze = [
    #     [0, 0, 0, 1],
    #     [1, 1, 0, 1],
    #     [0, 0, 0, 0],
    #     [1, 1, 1, 0]
    # ]

    maze = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    start = (0, 0)  # Starting position
    end = (3, 3)  # Target position

    print("Original Maze:")
    for row in maze:
        print(' '.join(['#' if cell == 1 else '.' for cell in row]))

    print("\nSearching for path from", start, "to", end)
    path = bfs_grid(maze, start, end)

    if path:
        print("\nPath found:", path)
        print("\nMaze with path (* represents the path):")
        print_path_in_maze(maze, path)
    else:
        print("\nNo path exists!")

# Run the example
if __name__ == "__main__":
    pass
