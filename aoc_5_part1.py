from collections import defaultdict

filename = 'aoc5data1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

d = defaultdict(list)
for text in texts:
    x, y = text.split('|')
    d[x].append(y)

# for k, v in d.items():
#     print(k, v)
rules = []
for text in texts:
    x, y = text.split('|')
    rules.append((x, y))
# for rule in rules:
#     print(rule)

###############################################################################

filename = 'aoc5data2.txt'
inf = open(filename)
nums = [[e for e in line.strip().split(',')] for line in inf]
inf.close()

valid_nums = []
invalid_nums = []
for e in nums:
    for i in range(len(e)):
        ok = True
        for j in range(i + 1, len(e)):
            if (e[i], e[j]) not in rules:
                ok = False
                break
        if not ok:
            break
    if ok:
        valid_nums.append(e)
    else:
        invalid_nums.append(e)

# print(valid_nums)
total = 0
for e in valid_nums:
    # print(e)
    # total += int(e[int((len(e) - 1) / 2)])
    total += int(e[int((len(e)) // 2)])
print(total)

###############################################################################
# part 2

sorted_nums = []
for e in invalid_nums:
    count_dict = defaultdict(int)
    for i in range(len(e)):
        for j in range(len(e)):
            if (e[i], e[j]) in rules:
                count_dict[e[i]] += 1
    # print(count_dict)
    # sorted1 = [(k, v) for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)]
    # print(sorted1)
    # sorted_nums.append([k for k, v in sorted1])
    sorted_nums.append([k for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)])

total = 0
for e in sorted_nums:
    total += int(e[int((len(e)) // 2)])
print(total)

# sample sorting dictionary by value
# >>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# >>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
