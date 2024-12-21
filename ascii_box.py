#            ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
#  length i  │  1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │  9 │ 10 │
#            ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  price  pi │  1 │  5 │  8 │  9 │ 10 │ 17 │ 17 │ 20 │ 24 │ 30 │
#            └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘


def draw_column_nums(n, width, left_width):
    print('*' * left_width + '  ', end='')  # * is dummy value because of problem in copy/paste
    # for i in range(n):
    #     print(' ' * int(width / 2), end='')
    #     print(i, end='')
    #     print(' ' * int(width / 2), end='')
    # print('')
    for i in range(n):
        print(f'{i:>{width - 1}}  ', end='')  # right-justify numbers
    print('')
    # for i in range(n):
    #     print(f'{i:{width}}  ', end='')
    # print('')


def draw_top(n, width, left_width):
    # print(' ' * left_width + ' ', end='')
    # print('┌', end='')
    # print(('─' * width + '┬') * (n - 1) + ('─' * width), end='')
    # print('┐')
    print(f'{" " * left_width} ┌{("─" * width + "┬") * (n - 1)}{"─" * width}┐')


def draw_mid(n, width, left_width):
    # print(' ' * left_width + ' ', end='')
    # print('├', end='')
    # print(('─' * width + '┼') * (n - 1) + ('─' * width), end='')
    # print('┤')
    print(f'{" " * left_width} ├{("─" * width + "┼") * (n - 1)}{"─" * width}┤')


def draw_bottom(n, width, left_width):
    # print(' ' * left_width + ' ', end='')
    # print('└', end='')
    # print(('─' * width + '┴') * (n - 1) + ('─' * width), end='')
    # print('┘')
    print(f'{" " * left_width} └{("─" * width + "┴") * (n - 1)}{"─" * width}┘')


def draw_data(arr, width, row, left_width):
    print(f'{row:>{left_width}} │', end='')
    for e in arr:
        if isinstance(e, list):
            e = str(e)
        if isinstance(e, str):
            print(f' {e:{width - 1}}│', end='')
        else:
            print(f'{e:>{width - 1}} │', end='')  # right-justify numbers
    print('')


def ascii_box(arr):
    width = max([len(str(e)) for subarr in arr for e in subarr]) + 2  # add 2 spaces
    left_width = len(str(len(arr)))
    n = len(arr[0])
    draw_column_nums(n, width, left_width)
    draw_top(n, width, left_width)
    for i in range(len(arr)):
        draw_data(arr[i], width, i, left_width)
        if i != len(arr) - 1:
            draw_mid(n, width, left_width)
    draw_bottom(n, width, left_width)


# def ascii_box1(arr):
#     # width = max([len(str(e)) for subarr in arr for e in subarr]) + 2  # add 2 spaces
#     maxlenarr = []
#     for col in range(len(arr[0])):
#         maxlencol = -sys.maxsize
#         for row in range(len(arr)):
#             maxlencol = max(maxlencol, len(str(arr[row][col])))
#         maxlenarr.append(maxlencol)
#
#     left_width = len(str(len(arr)))
#     n = len(arr[0])
#     for width in maxlenarr:
#         draw_column_nums(n, width, left_width)
#         draw_top(n, width, left_width)
#         for i in range(len(arr)):
#             draw_data(arr[i], width, i, left_width)
#             if i != len(arr) - 1:
#                 draw_mid(n, width, left_width)
#         draw_bottom(n, width, left_width)


# draw_top(10, 4)
# draw_data([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
# draw_bottom(10, 4)
# draw_mid(10, 4)
# ascii_box([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
# ascii_box([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

# ascii_box([[0, 0, 0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 1, 1, 1],
#            [0, 1, 1, 1, 1, 1, 1, 1],
#            [0, 1, 1, 1, 1, 1, 1, 1],
#            [0, 1, 1, 2, 2, 2, 2, 2],
#            [0, 1, 1, 2, 2, 3, 3, 3],
#            [0, 1, 1, 2, 2, 3, 3, 4]])


# ascii_box([[[''], [], [], []],
#            [[''], ['a'], [], []],
#            [[''], ['a', 'b'], ['ab'], []],
#            [[''], ['a', 'b', 'c'], ['ab', 'ac', 'bc'], ['abc']],
#            [[''], ['a', 'b', 'c', 'd'], ['ab', 'ac', 'bc', 'ad', 'bd', 'cd'], ['abc', 'abd', 'acd', 'bcd']]])

# print(''.join([str(i) + ' ' * 9 for i in range(10)]))
# print('   0   1   2   3   4   5   6   7   8   9' * 10)
#
# ascii_box([['h', 'e', 'r', 'e', ' ', 'i', 's', ' ', 'a', ' ', 's', 'i', 'm', 'p', 'l', 'e', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e']])
#
# ascii_box([['e', 'x', 'a', 'm', 'p', 'l', 'e']])

if __name__ == '__main__':
    # ascii_box([[[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #            [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #            [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #            [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]],
    #            [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]]])
    # ascii_box1([[[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]], [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]], [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]], [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]], [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]], [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]]])
    ascii_box([[1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5]])

    texts = '''............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............'''

    texts = [text for text in texts.split()]
    grid = [[c if c != '.' else ' ' for c in s] for s in texts]
    for e in grid:
        print(e)
    ascii_box(grid)
