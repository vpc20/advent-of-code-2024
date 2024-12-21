import re


# def left_wrap_around(wh, pos, left_steps):
#     while True:
#         left_steps -= 1
#         pos -= 1
#         if pos < 0:
#             pos = wh - 1
#         if left_steps == 0:
#             break
#     return pos


def solve_part1(arr, width, height):
    q1, q2, q3, q4 = 0, 0, 0, 0
    # final_pos = []
    for nums in arr:
        px, py = nums[0], nums[1]
        vx, vy = nums[2], nums[3]

        px = (px + vx * 100) % width
        py = (py + vy * 100) % height

        # if vx < 0:
        #     px = left_wrap_around(width, px, abs(vx) * 100)
        # else:
        #     px = (px + vx * 100) % width
        # if vy < 0:
        #     py = left_wrap_around(height, py, abs(vy) * 100)
        # else:
        #     py = (py + vy * 100) % height

        # if vx < 0:
        #     px = width - (abs(px + vx * 100) % width)
        # else:
        #     px = (px + vx * 100) % width
        # if vy < 0:
        #     py = width - (abs(py + vy * 100) % width)
        # else:
        #     py = (px + vy * 100) % height
        print(px, py)

        # print(final_pos)
        mid_width = width // 2
        mid_height = height // 2

        if px < mid_width and py < mid_height:
            q1 += 1
        if px > mid_width and py < mid_height:
            q2 += 1
        if px < mid_width and py > mid_height:
            q3 += 1
        if px > mid_width and py > mid_height:
            q4 += 1
    return q1 * q2 * q3 * q4


# parse text input
filename = 'aoc14data1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
# arr = [[c for c in line.strip()] for line in inf]
nums1 = [re.findall(r'-*\d+', line) for line in inf]
arr = [[int(nums2[0]), int(nums2[1]), int(nums2[2]), int(nums2[3])] for nums2 in nums1]
inf.close()

print(arr)
# for e in nums:
#     print(e)
# print(solve_part1(arr, 11, 7))
print(solve_part1(arr, 101, 103))
# 232589280
