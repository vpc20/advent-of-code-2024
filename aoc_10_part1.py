# bfs version
def hike_trail(grid, start_row, start_col):
    q = [(start_row, start_col)]
    seen = {(start_row, start_col)}
    score = 0

    while len(q) > 0:
        r, c = q.pop(0)
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:  # up, right, down, left
            if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == grid[r][c] + 1:
                if (nr, nc) in seen:  # comment out this portion for part 2
                    continue
                seen.add((nr, nc))
                if grid[nr][nc] == 9:
                    score += 1
                else:
                    q.append((nr, nc))

    return score

# bfs version, part 2
# def hike_trail(grid, start_row, start_col):
#     q = deque([(start_row, start_col)])
#     seen = {(start_row, start_col)}
#     score = 0
#
#     while len(q) > 0:
#         r, c = q.popleft()
#         for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:  # up, right, down, left
#             if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == grid[r][c] + 1:
#                 if grid[nr][nc] == 9:
#                     score += 1
#                 else:
#                     q.append((nr, nc)) # for part 2 only this statement is needed, comment out all statements below
#                     # if (nr, nc) not in seen:  # for part 1 this portion is needed, comment out above
#                     #     seen.add((nr, nc))
#                     #     q.append((nr, nc))
#
#     return score


# dfs version
# def hike_trail(grid, r, c):
#     seen = {(r, c)}
#     score = 0
#
#     def dfs(r, c):
#         nonlocal score
#         for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:  # up, right, down, left
#             if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == grid[r][c] + 1:
#                 if (nr, nc) in seen:  # for part 2 comment out this portion
#                     continue
#                 seen.add((nr, nc))
#                 if grid[nr][nc] == 9:
#                     score += 1
#                 else:
#                     dfs(nr, nc)
#         return
#
#     dfs(r, c)
#     return score


def solve_part1(grid):
    # starting points
    total_score = 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 0:
                total_score += hike_trail(grid, i, j)
    return total_score


# parse text input
filename = 'aoc10data1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
grid = [[int(c) for c in line.strip()] for line in inf]
inf.close()

nrows = len(grid)
ncols = len(grid[0])

# for e in grid:
#     print(e)


print(solve_part1(grid))
