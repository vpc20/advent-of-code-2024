def solve_part1(wire_values, operations):
    no_value_wires = set()
    for _, _, _, _, wire3 in operations:
        no_value_wires.add(wire3)

    new_set = set()
    while new_set != no_value_wires:
        for wire1, op, wire2, _, wire3 in operations:
            if wire1 in wire_values and wire2 in wire_values:
                if op == 'AND':
                    wire_values[wire3] = wire_values[wire1] & wire_values[wire2]
                    new_set.add(wire3)
                elif op == 'OR':
                    wire_values[wire3] = wire_values[wire1] | wire_values[wire2]
                    new_set.add(wire3)
                elif op == 'XOR':
                    wire_values[wire3] = wire_values[wire1] ^ wire_values[wire2]
                    new_set.add(wire3)

    print('wire values------------------------------')
    print(wire_values)

    z_wires = [[k, v] for k, v in wire_values.items() if k.startswith('z')]
    z_wires.sort(reverse=True)
    bit_str = ''.join(str(v) for w, v in z_wires)
    return int(bit_str, 2)


# f = open('aoc_23_test_data1.txt')
f = open('aoc_24_data1.txt')
# x = f.read()
input1, input2 = f.read().split('\n\n')

temp1 = [s.split(': ') for s in input1.split('\n')]
wire_values = {item[0]: int(item[1]) for item in temp1}
print(wire_values)

operations = [s.split(' ') for s in input2.split('\n')]
print(operations)
f.close()

result = solve_part1(wire_values, operations)
print(result)
