from collections import deque


def shortest_path(start, target, keypad):
    nrows = len(keypad)
    ncols = len(keypad[0])

    queue = deque([(start, '')])
    visited = {start}

    while queue:
        current, path = queue.popleft()
        if current == target:
            return path

        r, c = current
        for new_pos, direction in ([(r + 1, c), 'v'],
                                   [(r - 1, c), '^'],
                                   [(r, c + 1), '>'],
                                   [(r, c - 1), '<']):
            nr, nc = new_pos
            if 0 <= nr < nrows and 0 <= nc < ncols and new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, path + direction))

    return None


def numeric_keypad_path(code):
    numeric_keypad = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [None, '0', 'A']
    ]
    digit_position = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2)
    }

    start = digit_position['A']  # start position is 'A'
    path = ''

    for digit in code:
        path += shortest_path(start, digit_position[digit], numeric_keypad) + 'A'
        start = digit_position[digit]

    return path


def direction_keypad_path(num_key_path):
    direction_keypad = [
        [None, '^', 'A'],
        ['<', 'v', '>']
    ]
    direction_position = {
        '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2)
    }

    start = direction_position['A']  # start position is 'A'
    path = ''

    for c in num_key_path:
        path += shortest_path(start, direction_position[c], direction_keypad) + 'A'
        start = direction_position[c]

    return path


def main():
    codes = [
        "029A",
        "980A",
        "179A",
        "456A",
        "379A"
    ]
    # codes = [
    #     '671A',
    #     '826A',
    #     '670A',
    #     '085A',
    #     '283A'
    # ]

    total_complexity = 0

    # start_num_keypad = (3, 2)
    # start_dir_keypad = (0, 2)
    for code in codes:
        num_key_path = numeric_keypad_path(code)
        dir_key_path1 = direction_keypad_path(num_key_path)
        dir_key_path2 = direction_keypad_path(dir_key_path1)

        # numeric_part = int(code.replace('A', ''))
        print(len(dir_key_path2) , int(code[:3]))
        complexity = len(dir_key_path2) * int(code[:3])
        total_complexity += complexity

    print(f"Total complexity: {total_complexity}")


if __name__ == "__main__":
    main()
