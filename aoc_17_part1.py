def solve_part1(program, a, b, c):
    ip = 0
    output = []
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        combo_operand = 0
        if operand in [0, 1, 2, 3]:
            combo_operand = operand
        elif operand == 4:
            combo_operand = a
        elif operand == 5:
            combo_operand = b
        elif operand == 6:
            combo_operand = c
        elif operand == 7:
            combo_operand = 0

        if opcode == 0:
            a = a // (2 ** combo_operand)
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = combo_operand % 8
        elif opcode == 3:
            if a != 0:
                ip = operand
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(combo_operand % 8)
        elif opcode == 6:
            b = a // (2 ** combo_operand)
        elif opcode == 7:
            c = a // (2 ** combo_operand)

        ip += 2
    return output


# f = open('aoc_17_test_data1.txt')
f = open('aoc_17_data1.txt')
for line in f:
    if line.startswith('Register A'):
        a = int(line[12:])
    elif line.startswith('Register B'):
        b = int(line[12:])
    elif line.startswith('Register C'):
        c = int(line[12:])
    elif line.startswith('Program'):
        s = line[9:]
        program = [int(c) for c in s.split(',')]
f.close()

print(a)
print(b)
print(c)
print(program)

output = solve_part1(program, a, b, c)
print(output)
# print(','.join(output))
print(','.join([str(n) for n in output]))

# part 2
for a in range(1000000000):
    print(a)
    output = solve_part1(program, a, b, c)
    if output == program:
        print(a)
        break
