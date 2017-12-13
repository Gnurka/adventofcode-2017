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

def init_scanners(scanners, gates):
    for g in gates:
        depth = g[0]
        rng = g[1]

        diff = 1
        scanner = 0
        for i in range(0, depth):
            if scanner >= rng - 1 and diff == 1:
                diff = -1
            elif scanner == 0 and diff == -1:
                diff = 1

            scanner += diff

        scanners.append((scanner, diff))

def calc_severity(gates, delay, scanners):
    severity = 0
    for a, g in enumerate(gates):
        depth = g[0] + delay
        rng = g[1]

        diff = scanners[a][1]
        scanner = scanners[a][0]
        if scanner >= rng - 1 and diff == 1:
            diff = -1
        elif scanner == 0 and diff == -1:
            diff = 1

        scanner += diff
        scanners[a] = (scanner, diff)

        if scanner == 0:
            severity += depth * rng

    return severity


def star2(gates):
    scanners = []
    init_scanners(scanners, gates)

    #delay = 31000
    delay = 1
    while calc_severity(gates, delay, scanners) > 0:
        delay += 1
        if delay % 1000 == 0:
            print(delay)

    print(delay)

#print(star1(example, 10))

star2(gates)