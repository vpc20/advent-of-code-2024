# def solve_part1(arr, n):
#     print('blinking...')
#     i = 0
#     for bl in range(n):  # perform changes n times
#         print(f'blink...{bl+1}')
#         i = 0
#         while i < len(arr):
#             s = str(arr[i])
#             if arr[i] == 0:
#                 arr[i] = 1
#             elif len(s) % 2 == 0:
#                 mid = len(s) // 2
#                 first_num = int(s[:mid])
#                 second_num = int(s[mid:])
#                 first_arr = arr[:i]
#                 second_arr = arr[i:]
#                 first_arr += [first_num]
#                 second_arr[0] = second_num
#                 arr = first_arr + second_arr
#                 i += 1
#             else:
#                 arr[i] = arr[i] * 2024
#             i += 1
#         print(len(arr))
#     return len(arr)
from functools import cache


# simpler solution but inefficient
def solve_part1(arr, n):
    for bl in range(n):  # perform changes n times
        print(f'blink...{bl + 1}')
        result = []
        for i in range(len(arr)):
            s = str(arr[i])
            if arr[i] == 0:
                result.append(1)
            elif len(s) % 2 == 0:
                mid = len(s) // 2
                result.append(int(s[:mid]))
                result.append(int(s[mid:]))
            else:
                result.append(arr[i] * 2024)
        arr = result.copy()
        count = len(result)
        print(count)
        result.clear()
    return count


# efficient solution
def solve_part2(arr, n):
    @cache
    def dfs(val, n):
        if n == 0:
            return 1
        s = str(val)
        if val == 0:
            return dfs(1, n - 1)
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            return dfs(int(s[:mid]), n - 1) + dfs(int(s[mid:]), n - 1)
        else:
            return dfs(val * 2024, n - 1)

    stone_count = 0
    for e in arr:
        stone_count += dfs(e, n)
    return stone_count


# parse text input
filename = 'aoc11data1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
arr = [int(c) for line in inf for c in line.strip().split()]
inf.close()

print('input')
print(arr)

# aoc11testdata1.txt
# arr = [5] # test
# blink 25 times
print(solve_part1(arr, 25))
# 55312

# arr = [5] # test
print('part 2 solution')
print(solve_part2(arr, 75))
# 233007586663131
