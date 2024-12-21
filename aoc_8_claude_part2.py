from collections import defaultdict


def read_input(file_path):
    """Read and return grid from input file."""
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')


def find_antennas(grid):
    """Find all antenna positions grouped by frequency."""
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in '.#':
                antennas[grid[y][x]].append((x, y))
    return antennas


def is_collinear(p1, p2, p3):
    """Check if three points are collinear using cross product."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Calculate cross product
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)


def find_antinodes(grid):
    """Find all antinode locations in the grid."""
    height = len(grid)
    width = len(grid[0])
    antennas = find_antennas(grid)
    antinodes = set()

    # For each frequency
    for freq, positions in antennas.items():
        # Skip if there's only one antenna of this frequency
        if len(positions) < 2:
            continue

        # Check each point against each pair of antennas
        for x in range(width):
            for y in range(height):
                point = (x, y)
                # Count how many antennas are collinear with this point
                collinear_count = 0
                for i in range(len(positions)):
                    for j in range(i + 1, len(positions)):
                        if is_collinear(positions[i], positions[j], point):
                            collinear_count += 1
                            break
                    if collinear_count > 0:
                        break
                if collinear_count > 0:
                    antinodes.add(point)

        # Add antenna positions themselves as antinodes if there are multiple antennas
        if len(positions) > 1:
            antinodes.update(positions)
    return antinodes


def main(file_path):
    """Main function to process input file and return result."""
    grid = read_input(file_path)
    antinodes = find_antinodes(grid)
    print(antinodes)
    print('-------------------------------------------------------------------------')
    for e in sorted(antinodes):
        print(e)
    return len(antinodes)


# Test with example
example = """T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
.........."""


def test():
    grid = example.strip().split('\n')
    antinodes = find_antinodes(grid)
    result = len(antinodes)
    print(f"Test result: {result}")  # Should be 9 for this specific example


if __name__ == "__main__":
    # Test the example first
    # test()

    # Then process actual input file
    file_path = 'aoc8data1.txt'
    result = main(file_path)
    print(f"Total number of unique antinode locations: {result}")
