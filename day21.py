import math


def rotate_matrix(m):
    size = len(m)
    return [[row[size-1 - i] for row in m] for i in range(size)]


def flip_matrix_y(m):
    size = len(m)
    return [m[size-1-r] for r in range(3)]


def flip_matrix_x(m):
    return [list(reversed(r)) for r in m]


def divide_image(image, size):
    pieces = []
    for r in range(0,len(image),size):
        for c in range(0,len(image),size):
            pieces.append([[x[i] for i in range(c, c+size)] for x in image[r:r+size]])

    return pieces


def match_rules(image, pattern):
    for i, p in enumerate(pattern):
        if len(image) == len(p):
            rot1 = rotate_matrix(p)
            rot2 = rotate_matrix(rot1)
            rot3 = rotate_matrix(rot2)
            if (
                    image == p or
                    image == flip_matrix_x(p) or
                    image == flip_matrix_y(p) or
                    image == rot1 or
                    image == flip_matrix_x(rot1) or
                    image == flip_matrix_y(rot1) or
                    image == rot2 or
                    image == flip_matrix_x(rot2) or
                    image == flip_matrix_y(rot2) or
                    image == rot3 or
                    image == flip_matrix_x(rot3) or
                    image == flip_matrix_y(rot3)
            ):
                return i

    assert False, "No match found for %s." % image


def merge_pieces(new_pieces):
    size = int(math.sqrt(len(new_pieces)))

    if size == 1:
        return new_pieces[0]

    image = []
    for i in range(0,len(new_pieces),size):
        m = new_pieces[i:i+size]
        for r in range(len(m[0])):
            image.append(sum([m[i][r] for i in range(size)], []))

    return image


def string_to_matrix(string):
    return [[0 if i == '.' else 1 for i in x] for x in string.split("/")]


def parse_rules(input):
    rules = []
    results = []

    for line in input:
        parts = line.split(" => ")
        rules.append(string_to_matrix(parts[0]))
        results.append(string_to_matrix(parts[1]))

    return rules, results


#input = ["../.# => ##./#../...", ".#./..#/### => #..#/..../..../#..#"]
image = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]

with open('day21.txt') as fp:
    input = [x.rstrip() for x in fp]

rules, results = parse_rules(input)

for i in range(18):
    pieces = []
    if len(image) % 2 == 0:
        pieces = divide_image(image, 2)
    else:
        pieces = divide_image(image, 3)

    new_pieces = []
    for p in pieces:
        rule = match_rules(p, rules)
        new_pieces.append(results[rule])

    image = merge_pieces(new_pieces)
    print("Iteration %d, image size=%d" %(i+1, len(image)))


print("Lights on: %d" % sum([sum(x) for x in image]))