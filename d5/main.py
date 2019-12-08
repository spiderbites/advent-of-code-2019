import os

f = open(os.path.join(os.getcwd(), "input.txt"))
lines = f.read().strip().split(",")
original_intcodes = [int(line) for line in lines]


def run(input):
    def get_opcode(val):
        val = str(val).zfill(5)
        opcode = int(val[3] + val[4])
        c, b, a = int(val[2]), int(val[1]), int(val[0])
        return opcode, c, b, a

    intcodes = original_intcodes[:]
    position = 0
    opcode, c, b, a = get_opcode(intcodes[0])

    while opcode != 99:
        if opcode == 1:
            i, j = intcodes[position + 1], intcodes[position + 2]
            val_i = intcodes[i] if c == 0 else i
            val_j = intcodes[j] if b == 0 else j
            output_position = intcodes[position + 3]
            output_val = val_i + val_j
            intcodes[output_position] = output_val
            position += 4
        elif opcode == 2:
            i, j = intcodes[position + 1], intcodes[position + 2]
            val_i = intcodes[i] if c == 0 else i
            val_j = intcodes[j] if b == 0 else j
            output_position = intcodes[position + 3]
            output_val = val_i * val_j
            intcodes[output_position] = output_val
            position += 4
        elif opcode == 3:
            i = intcodes[position + 1]
            intcodes[i] = input
            position += 2
        elif opcode == 4:
            i = intcodes[position + 1]
            print(intcodes[i] if c == 0 else i)
            position += 2
        elif opcode == 5:
            first = intcodes[position + 1]
            second = intcodes[position + 2]
            val_first = intcodes[first] if c == 0 else first
            val_second = intcodes[second] if b == 0 else second
            if val_first != 0:
                position = val_second
            else:
                position += 3
        elif opcode == 6:
            first = intcodes[position + 1]
            second = intcodes[position + 2]
            val_first = intcodes[first] if c == 0 else first
            val_second = intcodes[second] if b == 0 else second
            if val_first == 0:
                position = val_second
            else:
                position += 3
        elif opcode == 7:
            first = intcodes[position + 1]
            second = intcodes[position + 2]
            third = intcodes[position + 3]
            val_first = intcodes[first] if c == 0 else first
            val_second = intcodes[second] if b == 0 else second
            intcodes[third] = 1 if val_first < val_second else 0
            position += 4
        elif opcode == 8:
            first = intcodes[position + 1]
            second = intcodes[position + 2]
            third = intcodes[position + 3]
            val_first = intcodes[first] if c == 0 else first
            val_second = intcodes[second] if b == 0 else second
            intcodes[third] = 1 if val_first == val_second else 0
            position += 4
        opcode, c, b, a = get_opcode(intcodes[position])

    return intcodes[0]


# p1
run(1)

# p2
run(5)
