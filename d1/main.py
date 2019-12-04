import math


def req(num):
    return math.floor(num / 3) - 2


def total_req(num):
    r = req(num)
    if r < 0:
        return num
    else:
        return num + total_req(r)


f = open("./input.txt")
lines = f.readlines()
nums = [int(line) for line in lines]

# p1
reqs = [req(num) for num in nums]
print(sum(reqs))

# p2
total_reqs = [total_req(r) for r in reqs]
print(sum(total_reqs))
