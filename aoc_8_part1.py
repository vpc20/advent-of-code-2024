from collections import defaultdict

from aoc_tools import read_input_to_grid


def find_antinodes(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    ax1 = x1 + (x1 - x2)
    ay1 = y1 + (y1 - y2)

    ax2 = x2 + (x2 - x1)
    ay2 = y2 + (y2 - y1)

    return (ax1, ay1), (ax2, ay2)


def find_antennas(grid):
    antennas = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                antennas[grid[i][j]].append((i, j))
    return antennas


def solve_part1(grid):
    antennas = find_antennas(grid)

    #  find antinode position for each pair of antennas with same frequency
    seen = set()
    for v in antennas.values():
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                antinodes = find_antinodes(v[i], v[j])
                for x, y in antinodes:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if (x, y) not in seen:
                            seen.add((x, y))
    return len(seen)


grid = read_input_to_grid('aoc8data1.txt')
print(solve_part1(grid))


# print(get_antinodes((1, 8), (2, 5)))
# print(get_antinodes((2, 5), (3, 7)))
