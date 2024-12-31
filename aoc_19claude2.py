from typing import Set, List


def count_arrangements_dp(design: str, patterns: Set[str]) -> int:
    """
    Use dynamic programming to count the number of ways to arrange towels.
    Returns only the count of possible arrangements.
    """
    n = len(design)
    # dp[i] stores number of ways to make substring from i to end
    dp = [0] * (n + 1)

    # Base case: empty string can be made in 1 way
    dp[n] = 1

    # Fill dp array from right to left
    for i in range(n - 1, -1, -1):
        for pattern in patterns:
            # Check if pattern can be placed at current position
            if i + len(pattern) <= n and design[i:i + len(pattern)] == pattern:
                dp[i] += dp[i + len(pattern)]

    return dp[0]


def solve_towel_arrangements(patterns: Set[str], designs: List[str]) -> int:
    """
    Calculate total number of possible arrangements for all designs.

    Args:
        patterns: Set of available towel patterns
        designs: List of desired designs to create

    Returns:
        Total number of possible arrangements across all designs
    """
    return sum(count_arrangements_dp(design, patterns) for design in designs)


# Example usage
def parse_input(input_text: str) -> tuple[Set[str], List[str]]:
    """Parse input text into patterns and designs."""
    lines = input_text.strip().split('\n')
    separator_idx = lines.index('')
    patterns = {p.strip() for p in lines[0].split(',')}
    designs = [d.strip() for d in lines[separator_idx + 1:]]
    return patterns, designs


# Example test input
example_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

filename = 'aoc_19_data1.txt'  # test - change
inf = open(filename)
input_data = inf.read()
inf.close()

# Test with example input
patterns, designs = parse_input(input_data)
result = solve_towel_arrangements(patterns, designs)
print(f"Total number of possible arrangements: {result}")