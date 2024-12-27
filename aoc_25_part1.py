def solve_part1(locks, keys):
    fit_count = 0
    for lock in locks:
        for key in keys:
            for i in range(5):
                if lock[i] + key[i] > 5:
                    break
            else:
                fit_count += 1

    return fit_count


f = open('aoc_25_data1.txt')
# f = open('aoc_25_data1.txt')
# x = f.read()
locks, keys = [], []
for text_grid in f.read().split('\n\n'):
    if text_grid[0] == '#':
        etype = 'lock'
    else:
        etype = 'key'
    heights = [-1 for _ in range(5)]
    for s in text_grid.split():
        for i, c in enumerate(s):
            if c == '#':
                heights[i] += 1
    if etype == 'lock':
        locks.append(heights)
    else:
        keys.append(heights)

print('locks', locks)
print('keys', keys)

result = solve_part1(locks, keys)
print(result)
