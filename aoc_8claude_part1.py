# from collections import defaultdict
# from typing import List, Set, Tuple
#
#
# def parse_input(grid: str) -> List[List[str]]:
#     """Convert input string to 2D grid."""
#     return [list(line.strip()) for line in grid.strip().split('\n')]
#
#
# def find_antennas(grid: List[List[str]]) -> dict:
#     """Find all antenna positions grouped by frequency."""
#     antennas = defaultdict(list)
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] not in '.':
#                 antennas[grid[y][x]].append((x, y))
#     return antennas
#
#
# def get_antinodes(p1: Tuple[int, int], p2: Tuple[int, int], width: int, height: int) -> Set[Tuple[int, int]]:
#     """Find antinodes for a pair of antennas."""
#     antinodes = set()
#     x1, y1 = p1
#     x2, y2 = p2
#
#     # Vector from p1 to p2
#     dx = x2 - x1
#     dy = y2 - y1
#
#     # Test both directions from both antennas
#     # From p1 towards p2 and beyond (2x distance)
#     x_node1 = x1 + 2 * dx
#     y_node1 = y1 + 2 * dy
#
#     # From p2 towards p1 and beyond (2x distance)
#     x_node2 = x2 - 2 * dx
#     y_node2 = y2 - 2 * dy
#
#     # # From p1 halfway to p2
#     # x_node3 = x1 + dx // 2
#     # y_node3 = y1 + dy // 2
#     #
#     # # From p2 halfway to p1
#     # x_node4 = x2 - dx // 2
#     # y_node4 = y2 - dy // 2
#
#     # Check all potential antinode positions
#     for x, y in [(x_node1, y_node1), (x_node2, y_node2)]:
#         if 0 <= x < width and 0 <= y < height:
#             antinodes.add((x, y))
#
#     return antinodes
#
#
# def calculate_antinodes(grid: List[List[str]], antennas: dict) -> Set[Tuple[int, int]]:
#     """Calculate all antinode positions."""
#     height = len(grid)
#     width = len(grid[0])
#     antinodes = set()
#
#     # Process each frequency group
#     for freq, positions in antennas.items():
#         # Check all pairs of antennas with same frequency
#         for i in range(len(positions)):
#             for j in range(i + 1, len(positions)):
#                 new_antinodes = get_antinodes(positions[i], positions[j], width, height)
#                 antinodes.update(new_antinodes)
#
#     return antinodes
#
#
# def print_grid_with_antinodes(grid: List[List[str]], antinodes: Set[Tuple[int, int]]) -> None:
#     """Print grid with antinodes marked as #."""
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if (x, y) in antinodes:
#                 print('#', end='')
#             elif grid[y][x] != '.':
#                 print(grid[y][x], end='')
#             else:
#                 print('.', end='')
#         print()
#
#
# def solve_antenna_problem(input_str: str, debug: bool = False) -> int:
#     """Main function to solve the antenna problem."""
#     grid = parse_input(input_str)
#     antennas = find_antennas(grid)
#     antinodes = calculate_antinodes(grid, antennas)
#
#     if debug:
#         print("\nGrid with antinodes marked:")
#         print_grid_with_antinodes(grid, antinodes)
#
#     return len(antinodes)
#
#
# # Test with example input
# example_input = """
# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# """
#
# # Run the solution with debug output
# result = solve_antenna_problem(example_input, debug=True)
# print(f"\nNumber of unique antinode locations: {result}")


from collections import defaultdict


def parse_input(grid):
    """Convert input string to 2D grid."""
    return [list(line.strip()) for line in grid.strip().split('\n')]


def find_antennas(grid):
    """Find all antenna positions grouped by frequency."""
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in '.':
                antennas[grid[y][x]].append((x, y))
    return antennas


def get_antinodes(p1, p2, width, height):
    """Find antinodes for a pair of antennas."""
    antinodes = set()
    x1, y1 = p1
    x2, y2 = p2

    # Vector from p1 to p2
    dx = x2 - x1
    dy = y2 - y1

    # From p1 towards p2 and beyond (2x distance)
    x_node1 = x1 + 2 * dx
    y_node1 = y1 + 2 * dy

    # From p2 towards p1 and beyond (2x distance)
    x_node2 = x2 - 2 * dx
    y_node2 = y2 - 2 * dy

    # Check all potential antinode positions
    for x, y in [(x_node1, y_node1), (x_node2, y_node2)]:
        if 0 <= x < width and 0 <= y < height:
            antinodes.add((x, y))

    return antinodes


def calculate_antinodes(grid, antennas):
    """Calculate all antinode positions."""
    height = len(grid)
    width = len(grid[0])
    antinodes = set()

    # Process each frequency group
    for freq, positions in antennas.items():
        # Check all pairs of antennas with same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                new_antinodes = get_antinodes(positions[i], positions[j], width, height)
                antinodes.update(new_antinodes)

    return antinodes


def solve_antenna_problem(input_str):
    """Main function to solve the antenna problem."""
    grid = parse_input(input_str)
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(grid, antennas)
    return len(antinodes)


def main():
    with open('aoc8data1.txt', 'r') as f:
        input_data = f.read()
    result = solve_antenna_problem(input_data)
    print(result)


if __name__ == "__main__":
    main()