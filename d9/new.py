#!./bin/python

import os

POSITION = 0
IMMEDIATE = 1
RELATIVE = 2

def run(input):
    def get_opcode(val):
        val = str(val).zfill(5)
        opcode = int(val[3] + val[4])
        c, b, a = int(val[2]), int(val[1]), int(val[0])
        return opcode, c, b, a

    def get_val(mode, parameter):
        if mode == POSITION:
            return intcodes[intcodes[parameter]]
        elif mode == IMMEDIATE:
            return intcodes[parameter]
        elif mode == RELATIVE:
            return intcodes[intcodes[parameter] + relative_base]

    def get_val_for_write(mode, parameter):
        if mode == POSITION:
            return intcodes[parameter]
        elif mode == IMMEDIATE:
            return parameter
        elif mode == RELATIVE:
            return intcodes[parameter] + relative_base

    intcodes = original_intcodes[:]
    pos = 0
    opcode, c, b, a = get_opcode(intcodes[0])
    relative_base = 0

    while opcode != 99:
        if opcode == 1:
            output_pos = get_val_for_write(a, pos + 3)
            intcodes[output_pos] = get_val(c, pos + 1) + get_val(b, pos + 2)
            pos += 4
        elif opcode == 2:
            output_pos = get_val_for_write(a, pos + 3)
            intcodes[output_pos] = get_val(c, pos + 1) * get_val(b, pos + 2)
            pos += 4
        elif opcode == 3:
            i = get_val_for_write(c, pos + 1)
            intcodes[i] = input
            pos += 2
        elif opcode == 4:
            output = get_val(c, pos + 1)
            print(output)
            pos += 2
        elif opcode == 5:
            val_first = get_val(c, pos + 1)
            val_second = get_val(b, pos + 2)
            if val_first != 0:
                pos = val_second
            else:
                pos += 3
        elif opcode == 6:
            val_first = get_val(c, pos + 1)
            val_second = get_val(b, pos + 2)
            if val_first == 0:
                pos = val_second
            else:
                pos += 3
        elif opcode == 7:
            val_first = get_val(c, pos + 1)
            val_second = get_val(b, pos + 2)
            output_pos = get_val_for_write(a, pos + 3)
            intcodes[output_pos] = 1 if val_first < val_second else 0
            pos += 4
        elif opcode == 8:
            val_first = get_val(c, pos + 1)
            val_second = get_val(b, pos + 2)
            output_pos = get_val_for_write(a, pos + 3)
            intcodes[output_pos] = 1 if val_first == val_second else 0
            pos += 4
        elif opcode == 9:
            offset = get_val(c, pos + 1)
            relative_base += offset
            pos += 2
        opcode, c, b, a = get_opcode(intcodes[pos])


if __name__ == "__main__":
    f = open(os.path.join(os.getcwd(), "d9/input.txt"))
    lines = f.read().strip().split(",")
    original_intcodes = [int(line) for line in lines]
    original_intcodes.extend([0]*100000)

    # p1
    run(1)

    # p2
    run(2)
