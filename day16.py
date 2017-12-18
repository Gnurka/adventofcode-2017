from time import time

def read_input(file):
    with open(file) as fp:
        return [line for line in fp]


def spin(programs, x):
    return programs[-x:]+programs[:-x]


def exchange(programs, a, b):
    swap(a, b, programs)


def swap(a, b, programs):
    tmp = programs[a]
    programs[a] = programs[b]
    programs[b] = tmp


def partner(programs, a, b):
    swap(programs.index(a), programs.index(b), programs)


def star1(input):
    programs = [chr(ord('a')+x) for x in range(16)]
    ops = input.split(',')

    for op in ops:
        if op[0] == 's':
            pass
            programs = spin(programs, int(op[1:]))
        elif op[0] == 'x':
            p = op[1:].split('/')
            exchange(programs, int(p[0]), int(p[1]))
        elif op[0] == 'p':
            p = op[1:].split('/')
            partner(programs, p[0], p[1])

    print("".join(programs))

    return programs


transform = star1(read_input('day16.txt')[0])


def star2(transform):
    start = time()

    programs = [chr(ord('a') + x) for x in range(16)]
    initial = programs
    seen = []

    for i in range(1000000000):
        s = "".join(programs)
        if s in seen:
            print(seen[1000000000 % i])
            return

        seen.append(s)

        next = ['a'] * 16
        #for j in range(16):
        #    next[transform.index(chr(ord('a') + j))] = programs[j]

        for j in range(16):
            next[j] = programs[ord(transform[j])-97]

        programs = next

        if programs == initial:
            print("Initial found at " + str(i))

        if i % 10000000 == 0:
            print("%d iterations in %s seconds." % (i, time() - start))

    print("".join(programs))

star2(transform)




def star22(input, iterations):
    programs = [chr(ord('a')+x) for x in range(16)]
    ops = input.split(',')
    seen = []

    for i in range(iterations):
        s = "".join(programs)
        if s in seen:
            print(seen[iterations % i])
            return

        seen.append(s)

        for op in ops:
            if op[0] == 's':
                pass
                programs = spin(programs, int(op[1:]))
            elif op[0] == 'x':
                p = op[1:].split('/')
                exchange(programs, int(p[0]), int(p[1]))
            elif op[0] == 'p':
                p = op[1:].split('/')
                partner(programs, p[0], p[1])

    print("".join(programs))

    return programs


transform = star22(read_input('day16.txt')[0], 1000000000)