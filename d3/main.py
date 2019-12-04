f = open("./input.txt")


def serialize(x, y):
    return f'{x}:{y}'


def serialize_steps(x, y, steps):
    return f'{x}:{y}:{steps}'


wire1 = f.readline().strip().split(",")
wire2 = f.readline().strip().split(",")


def draw_path(wire):
    x = 0
    y = 0
    path = set()
    step_map = {}
    steps = 0

    for instruction in wire:
        direction = instruction[0]
        distance = int(instruction[1:])
        for i in range(1, distance + 1):
            steps += 1
            if direction == 'U':
                y += 1
            if direction == 'D':
                y -= 1
            if direction == 'L':
                x -= 1
            if direction == 'R':
                x += 1
            serialized = serialize(x, y)
            if serialized not in path:
                path.add(serialized)
                step_map[serialized] = steps

    return path, step_map


(wire1_path, wire1_steps) = draw_path(wire1)
(wire2_path, wire2_steps) = draw_path(wire2)

# p1
intersections = wire1_path.intersection(wire2_path)
intersection_coords = [intersection.split(
    ":") for intersection in intersections]
intersection_distances = [abs(int(x)) + abs(int(y))
                          for x, y in intersection_coords]
print(min(intersection_distances))

# p2
total_intersection_steps = [wire1_steps[intersection] +
                            wire2_steps[intersection] for intersection in intersections]
print(min(total_intersection_steps))
