def snail(grid):
    if grid == [[]]:
        return []

    result = [grid[0][0]]
    visited = {(0, 0)}
    nrows = len(grid)
    ncols = len(grid[0])
    cell_count = nrows * ncols

    directions = [(0, +1), (+1, 0), (0, -1), (-1, 0)]
    dir_index = 0

    r, c = 0, 0
    while True:
        dr, dc = directions[dir_index]
        nr, nc = r + dr, c + dc
        if 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in visited:
            result.append(grid[nr][nc])
            visited.add((nr, nc))
            r, c = nr, nc
            if len(visited) == cell_count:
                break
        else:
            dir_index = (dir_index + 1) % 4

    return result


# array = [[1, 2, 3],
#          [8, 9, 4],
#          [7, 6, 5]]

# array = [[1, 2],
#          [4, 3]]

array = [[1, 2, 3],
         [6, 5, 4]]

# array = [[]]

print(snail(array))
