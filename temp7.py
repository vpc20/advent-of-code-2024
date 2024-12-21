import re
from itertools import product


def compute_tval(num, ops):
    result = num[0]
    for i in range(1, len(num)):
        if ops[i - 1] == '+':
            result += num[i]
        elif ops[i - 1] == '*':
            result *= num[i]
        elif ops[i - 1] == '||':
            result = result * 10 + num[i]
    return result


filename = 'aoc7data1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

nums1 = [re.findall(r'\d+', text) for text in texts]
tvals = [int(e[0]) for i, e in enumerate(nums1)]
nums = [[int(e) for e in ns] for ns in [e[1:] for e in nums1]]
print(tvals)
print(nums)


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
# print('compute tval')
# print(compute_tval([10, 19], ('*',)))