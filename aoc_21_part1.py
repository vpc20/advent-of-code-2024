from collections import deque

def find_shortest_path(start, target, keypad):
    """
    Finds the shortest path to reach a target position on a keypad.

    Args:
        start: Starting position on the keypad (tuple).
        target: Target position on the keypad (tuple).
        keypad: A dictionary representing the keypad layout.

    Returns:
        A string representing the shortest path using directional keys.
    """
    queue = deque([(start, '')])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == target:
            return path

        for direction, move in keypad[current].items():
            if move is not None:
                new_pos = move
                if new_pos not in visited:
                    visited.add(new_pos)
                    queue.append((new_pos, path + direction))

    return None

def robot_keypad_path(code):
    """
    Calculates the shortest path for a robot to type a given code on the numeric keypad.

    Args:
        code: The code to be typed (string).

    Returns:
        A string representing the shortest path for the robot.
    """
    robot_keypad = {
        (3, 1): {'^': (2, 1), 'v': (4, 1), '<': (3, 0), '>': (3, 2)},
        (3, 0): {'^': (2, 0), 'v': (4, 0), '>': (3, 1)},
        (3, 2): {'^': (2, 2), 'v': (4, 2), '<': (3, 1)},
        (2, 1): {'^': (1, 1), 'v': (3, 1), '<': (2, 0), '>': (2, 2)},
        (2, 0): {'^': (1, 0), 'v': (3, 0), '>': (2, 1)},
        (2, 2): {'^': (1, 2), 'v': (3, 2), '<': (2, 1)},
        (1, 1): {'^': None, 'v': (2, 1), '<': (1, 0), '>': (1, 2)},
        (1, 0): {'^': None, 'v': (2, 0), '>': (1, 1)},
        (1, 2): {'^': None, 'v': (2, 2), '<': (1, 1)},
        (4, 1): {'^': (3, 1), 'v': None, '<': (4, 0), '>': (4, 2)},
        (4, 0): {'^': (3, 0), 'v': None, '>': (4, 1)},
        (4, 2): {'^': (3, 2), 'v': None, '<': (4, 1)},
    }

    robot_start = (4, 2)  # Robot starts at 'A' in the bottom right corner
    robot_path = ''

    for digit in code:
        if digit == 'A':
            robot_path += 'A'
            continue

        digit_position = {
            '1': (1, 0), '2': (1, 1), '3': (1, 2),
            '4': (2, 0), '5': (2, 1), '6': (2, 2),
            '7': (3, 0), '8': (3, 1), '9': (3, 2),
            '0': (4, 1)
        }[digit]

        robot_path += find_shortest_path(robot_start, digit_position, robot_keypad)
        robot_start = digit_position

    return robot_path

def main():
    codes = [
        "029A",
        "980A",
        "179A",
        "456A",
        "379A"
    ]

    total_complexity = 0

    for code in codes:
        robot_path = robot_keypad_path(code)
        numeric_part = int(code.replace('A', ''))
        complexity = len(robot_path) * numeric_part
        total_complexity += complexity

    print(f"Total complexity: {total_complexity}")

if __name__ == "__main__":
    main()