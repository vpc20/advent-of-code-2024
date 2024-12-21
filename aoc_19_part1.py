# parse text input
from itertools import permutations

filename = 'aoc19testdata1.txt'  # test - change
inf = open(filename)
# texts = [line.strip() for line in inf]
# nums = [[int(e) for e in line.strip().split(',')] for line in inf]
# nums1 = [re.findall(r'-*\d+', line) for line in inf]
input_data = inf.read()
input1, input2 = input_data.split('\n\n')
inf.close()

# print(input1)
# print()
# print(input2)

patterns = input1.split(', ')
print(patterns)
# print(len(patterns))
designs = input2.split('\n')
# print(designs)

# brute force
# count = 0
# countp = 0
# for r in range(1, len(patterns)+1):
#     for p in permutations(patterns, r):
#         countp += 1
#         print(r, countp)
#         s = ''.join(p)
#         if s in designs:
#             count += 1
# print(count)

count = 0
countp = 1
for p in permutations(patterns):
    countp += 1
    print(countp)
    s = ''.join(p)
    if s in designs:
        count += 1
print(count)
