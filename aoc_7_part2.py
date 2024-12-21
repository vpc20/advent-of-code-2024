from itertools import product


def compute_tval(num, ops):
    result = num[0]
    for i in range(1, len(num)):
        if ops[i - 1] == '+':
            result += num[i]
        elif ops[i - 1] == '*':
            result *= num[i]
        elif ops[i - 1] == '||':
            # result = result * 10 + num[i]  ## incorrect
            result = int(str(result) + str(num[i]))
    return result


filename = 'aoc7data1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

nums1 = [s.replace(':', '').split() for s in texts]

tvals = [int(e[0]) for i, e in enumerate(nums1)]
nums = [[int(e) for e in ns] for ns in [e[1:] for e in nums1]]
print(tvals)
print(nums)

# s1 = set(list(permutations(['+', 'x', '+', 'x'], r=3)))
# print(s1)

# for p in permutations(['+', '*'], r=2):
#     print(p)

# for c in combinations(['+', '*'], r=2):
#     print(c)

# for c in combinations_with_replacement(['+', '*'], r=3):
#     print(c)

# for p in product(['+', '*'], repeat=3):
#     print(p)
# ops = list(product(['+', '*'], repeat=3))
# for e in ops:
#     print(e)
total = 0
for i, num in enumerate(nums):
    result = num[0]
    ops = list(product(['+', '*', '||'], repeat=len(num) - 1))
    for op in ops:
        result = compute_tval(num, op)
        if result == tvals[i]:
            total += result
            break

print(total)
# 61561126043536
