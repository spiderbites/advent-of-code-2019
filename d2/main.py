f = open("./input.txt")
lines = f.read().strip().split(",")
original_intcodes = [int(line) for line in lines]


def run(noun, verb):
    intcodes = original_intcodes[:]
    intcodes[1] = noun
    intcodes[2] = verb
    position = 0
    opcode = intcodes[0]
    while opcode != 99:
        i, j = intcodes[position + 1], intcodes[position + 2]
        val_i, val_j = intcodes[i], intcodes[j]
        output_position = intcodes[position + 3]
        if opcode == 1:
            output_val = val_i + val_j
        elif opcode == 2:
            output_val = val_i * val_j
        intcodes[output_position] = output_val
        position += 4
        opcode = intcodes[position]

    return intcodes[0]


# p1
result = run(12, 2)
print(result)

# p2


def p2():
    target = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = run(noun, verb)
            if result == target:
                answer = 100 * noun + verb
                return answer


print(p2())
