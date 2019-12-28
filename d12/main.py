#!./bin/python

# input
# <x=6, y=-2, z=-7>
# <x=-6, y=-7, z=-4>
# <x=-9, y=11, z=0>
# <x=-3, y=-4, z=6>


import numpy as np
import re
import os
from itertools import combinations


class Moon:
    def __init__(self, position, velocity):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def apply_velocity(self):
        self.position = self.velocity + self.position

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def potential_energy(self):
        return sum([abs(c) for c in self.position])

    def kinetic_energy(self):
        return sum([abs(c) for c in self.velocity])

    def __repr__(self):
        return f"p: {str(self.position)}, v: {str(self.velocity)}"


def apply_gravity(moons):
    pairs = combinations(moons, 2)
    for [p1, p2] in pairs:
        for i in range(3):
            if p1.position[i] > p2.position[i]:
                p1.velocity[i] -= 1
                p2.velocity[i] += 1
            elif p1.position[i] < p2.position[i]:
                p1.velocity[i] += 1
                p2.velocity[i] -= 1


def step(moons):
    apply_gravity(moons)
    for m in moons:
        m.apply_velocity()


def total_energy(moons):
    return sum([m.total_energy() for m in moons])


def find_cycle(moons, index):
    def serialize():
        return str([(m.velocity[index], m.position[index]) for m in moons])

    s = set()
    s.add(serialize())
    cycle = 1

    while True:
        length = len(s)
        step(moons)
        s.add(serialize())
        if length == len(s):
            return cycle
        cycle += 1


if __name__ == "__main__":
    f = open(os.path.join(os.getcwd(), "d12/input.txt")).readlines()
    inputs = [
        list(map(int, re.findall(r"(-?\d+)", line.strip('<>\n'))))
        for line in f
    ]
    moons = [Moon(position, [0, 0, 0]) for position in inputs]

    # p1
    for i in range(1000):
        step(moons)
    print(total_energy(moons))

    # p2
    c0 = find_cycle(moons, 0)
    c1 = find_cycle(moons, 1)
    c2 = find_cycle(moons, 2)

    # print(c0, c1, c2)
    print(np.lcm.reduce([c0, c1, c2]))
