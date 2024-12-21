# read text file

# filename = 'input.txt'
# inf = open(filename)
# arr = [[int(e) for e in line.split()] for line in inf]
# inf.close()
#
# print('[')# for e in arr:
#     print(e)
# print(']')

nums = []
filename = 'aoc1data.txt'
inf = open(filename)
for line in inf:
    nums.append([int(e) for e in line.split()])
# nums = [[int(e) for e in line.split()] for line in inf]  # one-liner
inf.close()

for e in nums:
    print(e)


