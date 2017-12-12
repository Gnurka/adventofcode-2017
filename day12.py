pipes = []

with open('day12.txt') as fp:
    for line in fp:
        program = int(line.split("<->")[0])
        connections = line.split("<->")[1].split(", ")
        pipes.extend([(program, int(x)) for x in connections])


def find_connections(group, program, pipes):
    if program in group:
        return

    group.add(program)

    for p in pipes:
        if program == p[0]:
            find_connections(group, p[1], pipes)
        elif program == p[1]:
            find_connections(group, p[0], pipes)


group0 = set()
find_connections(group0, 0, pipes)
print(len(group0), group0)


# Star 2 - brute force
groups = []
for p in pipes:
    group = set()
    find_connections(group, p[0], pipes)

    if group not in groups:
        groups.append(group)

print(len(groups))