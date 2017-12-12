example = "ne,ne,ne".split(",")


def oddq_to_cube(hexCol, hexRow):
    x = hexCol
    z = hexRow - (hexCol - (hexCol&1)) / 2
    y = -x-z
    return x, y, z


def cube_distance(x, y, z):
    return (abs(x) + abs(y) + abs(z)) / 2


def even(number):
    return number % 2 == 0


def star1(input):
    x = 0
    y = 0
    max_distance = 0
    for i in input:
        if i == "s":
            y += 1
        elif i == "n":
            y -= 1
        elif i == "ne":
            y -= 1 if even(x) else 0
            x += 1
        elif i == "se":
            y += 1 if not even(x) else 0
            x += 1
        elif i == "nw":
            y -= 1 if even(x) else 0
            x -= 1
        elif i == "sw":
            y += 1 if not even(x) else 0
            x -= 1

        a, b, c = oddq_to_cube(x, y)
        distance = cube_distance(a, b, c)
        if distance > max_distance:
            max_distance = distance

    print(x, y, oddq_to_cube(x, y), "max=" + str(max_distance))

star1(example)

with open('day11.txt') as fp:
    for line in fp:
        star1(line.rstrip().split(","))


