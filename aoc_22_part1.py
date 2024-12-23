def steps(secret_num):
    result = secret_num * 64
    secret_num ^= result
    secret_num %= 16777216

    result = secret_num // 32
    secret_num ^= result
    secret_num %= 16777216

    result = secret_num * 2048
    secret_num ^= result
    secret_num %= 16777216

    return secret_num


def solve_part1(grid):
    total = 0
    for n in nums:
        for _ in range(2000):
            sn = steps(n)
            n = sn
        total += sn
    return total


# f = open('aoc_22_test_data1.txt')
f = open('aoc_22_data1.txt')
nums = [int(line.strip()) for line in f]
print(nums)
f.close()

x = solve_part1(nums)
print(x)


