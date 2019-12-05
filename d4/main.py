def two_adjacent(num):
    return num[0] == num[1] or num[1] == num[2] or num[2] == num[3] or num[3] == num[4] or num[4] == num[5]


def non_decreasing(num):
    return num[0] <= num[1] <= num[2] <= num[3] <= num[4] <= num[5]


def exactly_two_adjacent(n):
    if two_adjacent(n):
        a = n[0] == n[1] and n[1] != n[2]
        b = n[1] == n[2] and n[0] != n[1] and n[2] != n[3]
        c = n[2] == n[3] and n[1] != n[2] and n[3] != n[4]
        d = n[3] == n[4] and n[2] != n[3] and n[4] != n[5]
        e = n[4] == n[5] and n[3] != n[4]
        return a or b or c or d or e
    else:
        return False


start = 206938
end = 679128

# p1
count = 0
for i in range(start, end+1):
    num = str(i)
    if non_decreasing(num) and two_adjacent(num):
        count += 1
print(count)

# p2
count = 0
for i in range(start, end+1):
    num = str(i)
    if non_decreasing(num) and exactly_two_adjacent(num):
        count += 1
print(count)
