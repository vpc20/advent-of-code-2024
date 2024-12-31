from functools import cache


@cache
def count_possible_ways(design, patterns):
    if design == '':
        return 1

    possible_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            possible_ways += count_possible_ways(design[len(pattern):], patterns)

    return possible_ways


# Example usage:
# patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
# designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
#
# result = count_possible_designs(patterns, designs)
# print(result)  # Output: 6


filename = 'aoc_19_data1.txt'  # test - change
inf = open(filename)
input_data = inf.read()
input1, input2 = input_data.split('\n\n')
inf.close()

patterns = input1.split(', ')
print(patterns)
designs = input2.split('\n')
print(designs)

total_count = 0
for design in designs:
    possible_count = count_possible_ways(design, tuple(patterns))
    total_count += possible_count  # Convert patterns to a tuple

print(total_count)
