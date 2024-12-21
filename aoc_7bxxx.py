from itertools import product


def concat_nums(num, ops):
    new_num = [num[0]]
    new_ops = []
    # numx = num[0]
    for i in range(1, len(num)):
        if ops[i - 1] == '||':
            if i == 1:
                new_num = []
            new_num.append(num[i-1] * 10 + num[i])
        elif ops[i - 1] == '+' or ops[i - 1] == '*':
            new_num.append(num[i])
            new_ops.append(ops[i - 1])
    return new_num, new_ops


def compute_tval(num, ops):
    result = num[0]
    for i in range(1, len(num)):
        if ops[i - 1] == '+':
            result += num[i]
        if ops[i - 1] == '*':
            result *= num[i]
    return result


filename = 'aoc7testdata1.txt'
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
        new_num, new_op = concat_nums(num, op)
        result = compute_tval(new_num, new_op)
        if result == tvals[i]:
            total += result
            break

print(total)
# print('compute tval')
# print(compute_tval([10, 19], ('*',)))
