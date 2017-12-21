import re


class Particle:
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.alive = True


def get_vector(string):
    return [int(x) for x in string.split(",")]


def vector_add(a, b):
    res = [0, 0, 0]
    res[0] = a[0] + b[0]
    res[1] = a[1] + b[1]
    res[2] = a[2] + b[2]
    return res


with open('day20.txt') as fp:
    particles = []
    for line in fp:
        pattern = re.compile('(?<=<).+?(?=>)')
        vectors = pattern.findall(line)
        pos = get_vector(vectors[0])
        vel = get_vector(vectors[1])
        acc = get_vector(vectors[2])
        particles.append(Particle(pos, vel, acc))


def check_collisions(particles):
    for ai, a in enumerate(particles):
        for bi, b in enumerate(particles):
            if ai != bi and a.pos[0] == b.pos[0] and a.pos[1] == b.pos[1] and a.pos[2] == b.pos[2]:
                a.alive = False
                b.alive = False


for i in range(100000):
    for p in particles:
        p.vel = vector_add(p.vel, p.acc)
        p.pos = vector_add(p.pos, p.vel)

    dist = [abs(p.pos[0]) + abs(p.pos[1]) + abs(p.pos[2]) for p in particles]
    min_dist = min(dist)
    min_index = dist.index(min_dist)

    check_collisions(particles)
    alive = sum([1 for x in particles if x.alive is True])

    print(min_dist, min_index, alive)