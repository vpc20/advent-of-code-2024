import re

import numpy as np


def compute_tokens(nums):
    ax, ay, bx, by, px, py = nums

    a = np.array([[ax, bx], [ay, by]])
    b = np.array([px, py])  # for part 2 multiply by 10000000000000

    solution = np.linalg.solve(a, b)
    token_count = solution[0] * 3 + solution[1] * 1
    return token_count


def solve_part1(arr):
    total_tokens = 0
    for nums in arr:
        token_count = compute_tokens(nums)
        if token_count.is_integer():
            # if token_count % 1 == 0:
            # if token_count == int(token_count):
            print(token_count)
            total_tokens += int(token_count)

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
# result is 25986, it should be 27105
