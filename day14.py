from functools import reduce


def reverse(circle, p1, p2):
    mid = int((p2-p1)/2)+1
    for i in range(0, mid):
        i1 = (p1 + i) % len(circle)
        i2 = (p2-i) % len(circle)
        circle[i1], circle[i2] = circle[i2], circle[i1]


def get_dense_hash(sparse):
    dense = []
    for i in range(0, 256, 16):
        sub = sparse[i:i+16]
        d = reduce((lambda a, b: a ^ b), sub)
        dense.append(d)

    return dense


def knot_hash_arr(lengths):
    suffix = [17, 31, 73, 47, 23]
    lengths.extend(suffix)

    pos = 0
    skip_length = 0
    list_size = 256
    circle = list(range(list_size))

    for a in range(64):
        for l in lengths:
            reverse(circle, pos, pos + l - 1)
            pos = (pos + l + skip_length) % list_size
            skip_length += 1

    dense = get_dense_hash(circle)
    dense_hex = [format(x, '02x') for x in dense]
    return "".join(dense_hex)


def knot_hash(inputstr):
    return knot_hash_arr([ord(i) for i in inputstr])


def star1(input):
    used = 0
    for i in range(128):
        hash = knot_hash(input + "-" + str(i))
        used += str(bin(int(hash, 16))).count('1')

    print(used)


def find_next_region(row, col, memory):
    for i, r in enumerate(memory):
        try:
            c = r.index(1)
            return (i, c)
        except:
            pass

    return None


def mark_region(region_nr, row, col, memory):
    assert memory[row][col] == 1

    memory[row][col] = region_nr

    if col > 0 and memory[row][col-1] == 1:
        mark_region(region_nr, row, col-1, memory)

    if col < len(memory[row])-2 and memory[row][col+1] == 1:
        mark_region(region_nr, row, col+1, memory)

    if row > 0 and memory[row-1][col] == 1:
        mark_region(region_nr, row-1, col, memory)

    if row < len(memory)-2 and memory[row+1][col] == 1:
        mark_region(region_nr, row+1, col, memory)


def star2(input):
    memory = []
    for i in range(128):
        hash = knot_hash(input + "-" + str(i))
        memory.append([int(x) for x in "".join([format(int(x, 16), '04b') for x in hash])])

    region_nr = 2
    i = find_next_region(0, 0, memory)
    while i is not None:
        mark_region(region_nr, i[0], i[1], memory)
        region_nr += 1
        i = find_next_region(i[0], i[1], memory)

    for row in memory:
        print(row)


#star1("ljoxqyyw")
star2("ljoxqyyw")