with open('day13.txt') as fp:
    gates = [[int(x) for x in line.split(": ")] for line in fp]


example = [[0, 3], [1, 2], [4, 4], [6, 4]]


def star1(gates, delay):
    severity = 0
    for g in gates:
        depth = g[0] + delay
        rng = g[1]

        diff = 1
        scanner = 0
        for i in range(0, depth):
            if scanner >= rng-1 and diff == 1:
                diff = -1
            elif scanner == 0 and diff == -1:
                diff = 1

            scanner += diff

        if scanner == 0:
            severity += depth * rng

    return severity


def star2(gates):
    delay = 0
    while star1(gates, delay) > 0:
        delay += 1
        if delay % 1000 == 0:
            print(delay)

    print(delay)

#print(star1(example, 10))

star2(gates)