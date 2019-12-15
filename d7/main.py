import os
import itertools


def runp1(*inputs):
    def get_opcode(val):
        val = str(val).zfill(5)
        opcode = int(val[3] + val[4])
        c, b, a = int(val[2]), int(val[1]), int(val[0])
        return opcode, c, b, a

    intcodes = original_intcodes[:]
    position = 0
    opcode, c, b, a = get_opcode(intcodes[0])
    input_index = 0

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
            intcodes[i] = inputs[input_index]
            input_index += 1
            position += 2
        elif opcode == 4:
            i = intcodes[position + 1]
            output = intcodes[i] if c == 0 else i
            return intcodes[i] if c == 0 else i
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


def runp2(inputs, position, intcodes):
    def get_opcode(val):
        val = str(val).zfill(5)
        opcode = int(val[3] + val[4])
        c, b, a = int(val[2]), int(val[1]), int(val[0])
        return opcode, c, b, a

    opcode, c, b, a = get_opcode(intcodes[position])
    current_inputs = inputs[:]

    current_output = None

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
            intcodes[i] = current_inputs.pop(0)
            position += 2
        elif opcode == 4:
            i = intcodes[position + 1]
            current_output = intcodes[i] if c == 0 else i
            position += 2
            # return the current output and the current state
            return (False, [current_output, position, intcodes, current_inputs])
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

    return (True, current_output)


if __name__ == "__main__":
    f = open(os.path.join(os.getcwd(), "d7/input.txt"))
    lines = f.read().strip().split(",")
    original_intcodes = [int(line) for line in lines]

    # p1
    combos = itertools.permutations([0, 1, 2, 3, 4], 5)
    outputs = []
    for combo in combos:
        prev_result = 0
        for i in combo:
            result = runp1(i, prev_result)
            prev_result = result
        outputs.append(prev_result)

    print(max(outputs))

    # p2

    INPUTS = 0
    POSITION = 1
    INTCODES = 2

    phases = itertools.permutations([5, 6, 7, 8, 9], 5)

    signals = []

    for phase in phases:
        amplifiers = [[[p], 0, original_intcodes[:]] for p in phase]

        # add initial input to amp 1..
        amplifiers[0][0].append(0)

        amplifier_index = 0

        done = False

        last_output = None

        while not done:
            current_amp = amplifiers[amplifier_index]
            (done, state) = runp2(
                current_amp[INPUTS],
                current_amp[POSITION],
                current_amp[INTCODES]
            )

            if done:
                signals.append(last_output)
            else:
                amplifiers[amplifier_index][POSITION] = state[1]
                amplifiers[amplifier_index][INTCODES] = state[2]
                amplifiers[amplifier_index][INPUTS] = state[3]

                if amplifier_index == 4:
                    last_output = state[0]

                amplifier_index = (amplifier_index + 1) % 5

                # add input for next amplifier using output from previous
                amplifiers[amplifier_index][INPUTS].append(state[0])

    print(max(signals))
