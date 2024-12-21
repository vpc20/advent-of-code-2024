from itertools import permutations


def count_possible_designs(patterns, designs):
    """
    Counts the number of possible designs given a list of available patterns and desired designs.

    Args:
        patterns: A list of strings representing available towel patterns.
        designs: A list of strings representing desired designs.

    Returns:
        The number of possible designs.
    """

    def is_possible(design, patterns):
        """
        Checks if a given design is possible using the available patterns.

        Args:
            design: The desired design.
            patterns: The available patterns.

        Returns:
            True if the design is possible, False otherwise.
        """

        if design == '':
            return True

        for pattern in patterns:
            if design.startswith(pattern) and is_possible(design[len(pattern):], patterns):
                return True

        return False

    count = 0
    for design in designs:
        if is_possible(design, patterns):
            count += 1

    return count


# Example usage:
# patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
# designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
#
# result = count_possible_designs(patterns, designs)
# print(result)  # Output: 6

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

result = count_possible_designs(patterns, designs)
print(result)  # Output: 6



