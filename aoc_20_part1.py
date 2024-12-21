from aoc_tools import read_input_to_grid, print_grid, print_grid_as_text, print_grid_with_tabs


def solve_part1(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    # find starting position
    r, c = 0, 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 'S':
                r = i
                c = j
                break
        else:
            continue
        break
    print('start_row', r, 'start_col', c)

    # update maze with steps number
    steps = 0
    end_found = False
    tracks = {(r, c)}
    grid[r][c] = 0  # step 0
    while not end_found:
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if grid[nr][nc] == 'E':
                    steps += 1
                    grid[nr][nc] = steps
                    tracks.add((nr, nc))
                    end_found = True
                if grid[nr][nc] == '.':
                    steps += 1
                    grid[nr][nc] = steps
                    tracks.add((nr, nc))
                    # print('track added', (nr, nc))
                    r, c = nr, nc
                    break
    print(tracks)
    print_grid_with_tabs(grid)

    # try removing walls for each step and calculate time saved in picoseconds
    count = 0
    for track in tracks:
        print('track', track)
        r, c = track
        for nr, nc in ((r - 1, c - 1), (r - 2, c), (r - 1, c + 1),
                       (r, c - 2), (r, c + 2),
                       (r + 1, c - 1), (r + 2, c), (r + 1, c + 1)):
            if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] != '#':
                # if not grid[r][c].isnumeric():
                #     print('grid[r][c]', grid[r][c])
                # if not grid[nr][nc].isnumeric():
                #     print('grid[nr][nc]', grid[nr][nc])
                if int(grid[nr][nc]) - int(grid[r][c]) >= 102:
                    count += 1
    return count


grid = read_input_to_grid('aoc_20_test_data1.txt')
print_grid(grid)
print_grid_as_text(grid)

x = solve_part1(grid)
print(x)
