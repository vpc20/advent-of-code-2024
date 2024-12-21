# from functools import cache


# @cache
def count_recursive(patterns, design, index=0):
    """
    Recursively counts the number of ways to create a design.

    Args:
        patterns: A list of available towel patterns.
        design: The target design.
        index: The current index in the design.

    Returns:
        The number of ways to create the design.
    """

    if index == len(design):
        return 1  # Base case: empty design

    count = 0
    for pattern in patterns:
        if design.startswith(pattern, index):
            count += count_recursive(patterns, design, index + len(pattern))

    return count


# Example usage:
# patterns = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
# design1 = 'brwrr'
# design2 = 'rrbgbr'
#
# result1 = count_recursive(patterns, design1)
# result2 = count_recursive(patterns, design2)
#
# print(result1)  # Output: 2
# print(result2)  # Output: 6

###################################################################################################
# parse text input

filename = 'aoc19data1.txt'  # test - change
inf = open(filename)
input_data = inf.read()
input1, input2 = input_data.split('\n\n')
inf.close()

# print(input1)
# print()
# print(input2)

patterns = input1.split(', ')
print(patterns)
# print(len(patterns))
designs = input2.split('\n')
print(designs)

total_count = 0
for design in designs:
    print(design)
    total_count += count_recursive(patterns, design, index=0)
print(total_count)
