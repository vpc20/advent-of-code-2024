import re

import numpy as np


# def compute_tokens(nums, counta, countb):
#     token_count = 0
#     ax, ay, bx, by, px, py = nums
#     if ax * counta + bx * countb == px and ay * counta + by * countb == py:
#         token_count = counta * 3 + countb * 1
#     return token_count


def solve_part1(arr):
    total_tokens = 0
    for nums in arr:
        ax, ay, bx, by, px, py = nums
        px += 10000000000000
        py += 10000000000000
        a = np.array([[ax, bx], [ay, by]])
        b = np.array([px, py])
        x = np.linalg.solve(a, b)
        print(x)
        counta, countb = x
        if counta % 1 == 0 and countb % 1 == 0:
            total_tokens += int(counta) * 3 + int(countb) * 1

    return total_tokens


# parse text input
filename = 'aoc13data1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
# arr = [[c for c in line.strip()] for line in inf]
nums1 = [re.findall(r'\d+', line) for line in inf]
nums2 = [nums1[i] + nums1[i + 1] + nums1[i + 2] for i in range(0, len(nums1), 4)]
arr = [[int(e) for e in num] for num in nums2]
inf.close()

# for e in nums:
#     print(e)
print(arr)
print(solve_part1(arr))
# 27105
