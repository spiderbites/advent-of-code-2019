#!./bin/python

import os
from PIL import Image

POSITION = 0
IMMEDIATE = 1
RELATIVE = 2


class Robot:
    LEFT = 0
    RIGHT = 1
    BLACK = 0
    WHITE = 1

    def __init__(self, squares={}):
        self.squares = squares
        self.position = [0, 0]
        self.direction = 'U'

    def serialize(self, x):
        return str(x)

    def deserialize(self, x):
        return eval(x)

    def current_color(self):
        return self.squares.get(self.serialize(self.position)) or Robot.BLACK

    def paint(self, color):
        self.squares[self.serialize(self.position)] = color

    def turn(self, t):
        if self.direction == 'U' and t == Robot.LEFT:
            self.direction = 'L'
        elif self.direction == 'U' and t == Robot.RIGHT:
            self.direction = 'R'
        elif self.direction == 'L' and t == Robot.LEFT:
            self.direction = 'D'
        elif self.direction == 'L' and t == Robot.RIGHT:
            self.direction = 'U'
        elif self.direction == 'R' and t == Robot.LEFT:
            self.direction = 'U'
        elif self.direction == 'R' and t == Robot.RIGHT:
            self.direction = 'D'
        elif self.direction == 'D' and t == Robot.LEFT:
            self.direction = 'R'
        elif self.direction == 'D' and t == Robot.RIGHT:
            self.direction = 'L'

    def move(self):
        X = 0
        Y = 1
        if self.direction == 'U':
            self.position[Y] += 1
        elif self.direction == 'D':
            self.position[Y] -= 1
        elif self.direction == 'L':
            self.position[X] -= 1
        elif self.direction == 'R':
            self.position[X] += 1

    def show_map(self):
        squares = self.squares.copy()

        # make all coords positive
        coords = [self.deserialize(c) for c in squares.keys()]
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        min_x = min(xs)
        min_y = min(ys)
        increase_by = -min(min_x, min_y)

        row = 50 * [0]
        data = [row.copy() for i in range(8)]

        for (k, v) in squares.items():
            [x, y] = self.deserialize(k)
            new_x = (x + increase_by)
            new_y = (y + increase_by)
            data[new_y][new_x] = v

        cmap = {0: (0, 0, 0),
                1: (255, 255, 255)}
        img = Image.new('RGB', (50, 8), "white")
        flat = [cmap[num] for row in data for num in row]
        img.putdata(flat)
        img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
        img.show()


def run(robot):
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

    # robot stuff
    OUTPUT_TYPE_PAINT = True
    OUTPUT_TYPE_MOVE = False
    current_output_type = OUTPUT_TYPE_PAINT

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
            intcodes[i] = robot.current_color()
            pos += 2
        elif opcode == 4:
            output = get_val(c, pos + 1)
            if current_output_type == OUTPUT_TYPE_PAINT:
                robot.paint(output)
            else:
                robot.turn(output)
                robot.move()
            current_output_type = not current_output_type
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

    return robot.squares


if __name__ == "__main__":
    f = open(os.path.join(os.getcwd(), "d11/input.txt"))
    lines = f.read().strip().split(",")
    original_intcodes = [int(line) for line in lines]
    original_intcodes.extend([0]*100000)

    # p1
    robot = Robot()
    run(robot)
    print(len(robot.squares))

    # p2
    robot = Robot(squares={"[0, 0]": Robot.WHITE})
    run(robot)
    robot.show_map()
