def count_design_arrangements(patterns, design):
    """
    Counts the number of ways to arrange towels for a single design.

    Args:
        patterns: A list of available towel patterns.
        design: The desired design.

    Returns:
        The number of arrangements for the design.
    """

    dp = [0] * (len(design) + 1)
    pattern_lengths = [len(pattern) for pattern in patterns]

    dp[0] = 1  # Empty design can be constructed in one way

    for i in range(1, len(design) + 1):
        for k in range(len(patterns)):
            if i >= pattern_lengths[k] and design[i - pattern_lengths[k]:i] == patterns[k]:
                dp[i] += dp[i - pattern_lengths[k]]

    return dp[-1]


# Example usage:
patterns = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
design1 = 'brwrr'
design2 = 'rrbgbr'

result1 = count_design_arrangements(patterns, design1)
result2 = count_design_arrangements(patterns, design2)

print(result1)  # Output: 2
print(result2)  # Output: 6

###################################################################################################
# parse text input

# filename = 'aoc19data1.txt'  # test - change
# inf = open(filename)
# input_data = inf.read()
# input1, input2 = input_data.split('\n\n')
# inf.close()
#
# # print(input1)
# # print()
# # print(input2)
#
# patterns = input1.split(', ')
# print(patterns)
# # print(len(patterns))
# designs = input2.split('\n')
# print(designs)
#
# total_count = 0
# for design in designs:
#     print(design)
#     total_count += count_design_arrangements(patterns, design)
# print(total_count)