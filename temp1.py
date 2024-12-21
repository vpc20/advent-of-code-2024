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

    rows, cols = len(grid), len(grid[0])

    # Check if start and end are valid
    if (not (0 <= start[0] < rows and 0 <= start[1] < cols) or
            not (0 <= end[0] < rows and 0 <= end[1] < cols) or
            grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1):
        return None

    # Possible movements: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Queue for BFS
    queue = deque([(start, [start])])
    # Keep track of visited cells
    visited = {start}

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        # If we reached the end, return the path
        if (curr_row, curr_col) == end:
            return path

        # Try all possible directions
        for d_row, d_col in directions:
            next_row, next_col = curr_row + d_row, curr_col + d_col
            next_pos = (next_row, next_col)

            # Check if the next position is valid and unvisited
            if (0 <= next_row < rows and
                    0 <= next_col < cols and
                    grid[next_row][next_col] == 0 and
                    next_pos not in visited):
                queue.append((next_pos, path + [next_pos]))
                visited.add(next_pos)

    # No path found
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