#!./bin/python

from operator import itemgetter
from itertools import groupby
import math

ASTERIOD = '#'


def parse(filepath):
    asteriods = []
    with open(filepath) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for (row, line) in enumerate(lines):
            for (col, item) in enumerate(line):
                if item == ASTERIOD:
                    asteriods.append([col, row])
    return asteriods


def serialize(x):
    return str(x)


def deserialize(x):
    return eval(x)


def count_visible(asteroids):
    totals = {}
    for a in asteroids:
        slopes = set()
        for b in asteroids:
            if a == b:
                continue
            slopes.add(slopeish(a, b))
        totals[serialize(a)] = len(slopes)
    return totals


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def slopes_for_station(station, asteroids):
    slopes = []
    for a in asteroids:
        if a == station:
            continue
        slope = slopeish2(station, a)
        slopes.append((slope, dist(station, a), a))
    sorted_slopes = sorted(slopes)
    groups = groupby(sorted_slopes, key=itemgetter(0))
    return groups


def slopeish(a, b):
    if a[0] == b[0]:
        return 'inf' if a[1] > b[1] else '-inf'
    if a[1] == b[1]:
        return '0' if a[0] > b[0] else '-0'
    slope = (a[1] - b[1]) / (a[0] - b[0])
    if a[0] < b[0]:
        return '<' + str(slope)
    else:
        return '>' + str(slope)


# give the slopes an order so we vaporize asteroids
# in the right order. The ordering is a bit funny
# because 0,0 is the top left, not the center.
#
#   h  a  b
#   g  X  c
#   f  e  d
#
def slopeish2(a, b):
    if a[0] == b[0]:
        return ('a', math.inf) if a[1] > b[1] else ('e', -math.inf)
    if a[1] == b[1]:
        return ('g', 0) if a[0] > b[0] else ('c', -0)
    slope = (a[1] - b[1]) / (a[0] - b[0])
    if slope > 0 and a[0] < b[0]:
        return ('d', slope)
    elif slope < 0 and a[0] < b[0]:
        return ('b', slope)
    elif slope > 0 and a[0] > b[0]:
        return ('h', slope)
    else:
        return ('f', slope)


def vaporize(asteroids):
    i = 0
    vape_count = 0
    while len(asteroids) > 0:
        i = (i % len(asteroids))
        vape_count += 1
        asteroid = asteroids[i].pop(0)
        if vape_count == 200:
            return asteroid
        if len(asteroids[i]) == 0:
            asteroids.pop(i)
        else:
            i += 1


if __name__ == "__main__":
    asteriods = parse("./d10/input.txt")
    totals = count_visible(asteriods)

    # p1
    station = max(totals.items(), key=itemgetter(1))
    print(station[1])

    # p2
    station_coords = deserialize(station[0])
    grouped_slopes = slopes_for_station(station_coords, asteriods)

    # drop the distance and the slope since we're all sorted
    # and just keep the the co-ordinate
    ordered_coords = [[i[2] for i in list(g)] for (k, g) in grouped_slopes]
    two_hundo = vaporize(ordered_coords)
    print(two_hundo[0] * 100 + two_hundo[1])
