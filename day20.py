import re

class Particle:
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc


def get_vector(string):
    return [int(x) for x in string[1:-1].split(",")]


def vector_add(a, b):
    res = [0, 0, 0]
    res[0] = a[0] + b[0]
    res[1] = a[1] + b[1]
    res[2] = a[2] + b[2]
    return res


with open('day20.txt') as fp:
    particles = []
    for line in fp:
        pattern = re.compile('<.+?>')
        vectors = pattern.findall(line)
        pos = get_vector(vectors[0])
        vel = get_vector(vectors[1])
        acc = get_vector(vectors[2])
        particles.append(Particle(pos, vel, acc))


for i in range(100000):
    min_index = 0
    min_dist = 1000000

    for pi, p in enumerate(particles):
        p.vel = vector_add(p.vel, p.acc)
        p.pos = vector_add(p.pos, p.vel)

        dist = abs(p.pos[0]) + abs(p.pos[1]) + abs(p.pos[2])
        if dist < min_dist:
            min_dist = dist
            min_index = pi

    print(min_dist, min_index)