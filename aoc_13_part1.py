import re
import sys


def compute_tokens(nums, counta, countb):
    token_count = 0
    ax, ay, bx, by, px, py = nums
    if ax * counta + bx * countb == px and ay * counta + by * countb == py:
        token_count = counta * 3 + countb * 1
    return token_count


def solve_part1(arr):
    total_tokens = 0
    for nums in arr:
        min_token_count = sys.maxsize
        for counta in range(101):
            for countb in range(101):
                token_count = compute_tokens(nums, counta, countb)
                if token_count != 0:
                    min_token_count = min(min_token_count, token_count)
        if min_token_count < sys.maxsize:
            print(min_token_count)
            total_tokens += min_token_count
    return total_tokens


# parse text input
filename = 'aoc_13_data1.txt'
inf = open(filename)
nums1 = [re.findall(r'\d+', line) for line in inf]
nums2 = [nums1[i] + nums1[i + 1] + nums1[i + 2] for i in range(0, len(nums1), 4)]
arr = [[int(e) for e in num] for num in nums2]
inf.close()

# for e in nums:
#     print(e)
print(arr)
print(solve_part1(arr))
# 27105
