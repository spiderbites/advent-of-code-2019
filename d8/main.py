import os
from PIL import Image


def chunks(s, n):
    """Yield successive n-sized chunks from s."""
    for i in range(0, len(s), n):
        yield s[i:i + n]


def count_occurrence(lst, item):
    return len([i for i in lst if i == item])


if __name__ == "__main__":
    f = open(os.path.join(os.getcwd(), "d8/input.txt"))
    digits = [int(d) for d in f.read().strip()]
    w = 25
    h = 6

    layers = list(chunks(digits, w*h))

    # p1
    num_zeros = [count_occurrence(l, 0) for l in layers]
    min_zero_index = num_zeros.index(min(num_zeros))
    num_ones = count_occurrence(layers[min_zero_index], 1)
    num_twos = count_occurrence(layers[min_zero_index], 2)
    print(num_ones * num_twos)

    # p2
    black = 0
    white = 1
    trans = 2

    def first_color(lst):
        for c in lst:
            if c != trans:
                return c
        return trans

    zipped = [z for z in zip(*layers)]
    colors = [str(first_color(z)) for z in zipped]

    cmap = {'0': (255, 255, 255),
            '1': (0, 0, 0)}

    data = [cmap[letter] for letter in colors]
    img = Image.new('RGB', (w, h), "white")
    img.putdata(data)
    img.show()
