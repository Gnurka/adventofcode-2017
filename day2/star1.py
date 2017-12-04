
example1 = r"""5 1 9 5
7 5 3
2 4 6 8"""

example2 = r"""5 9 2 8
9 4 7 3
3 8 6 5"""

def read_lines(file):
    with open(file) as fp:
        return [line for line in fp]


def star1():
    checksum = 0
    lines = read_lines('input.txt')
    for line in lines:
        x = [int(x) for x in line.split('\t')]
        x.sort()
        diff = x[-1] - x[0]
        checksum += diff

    print(checksum)


def evenly_divide(numbers):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i == j:
                continue

            div = x / y
            if div == round(div):
                return div


def star2():
    checksum = 0
    #lines = example2.split('\n')
    lines = read_lines('input.txt')
    for line in lines:
        x = [int(x) for x in line.split('\t')]
        x.sort(reverse=True)
        checksum += evenly_divide(x)

    print(checksum)


star2()