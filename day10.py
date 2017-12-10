from functools import reduce

input = [83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100]
inputstr = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"
suffix = [17, 31, 73, 47, 23]


def reverse(circle, p1, p2):
    mid = int((p2-p1)/2)+1
    for i in range(0, mid):
        i1 = (p1 + i) % len(circle)
        i2 = (p2-i) % len(circle)
        circle[i1], circle[i2] = circle[i2], circle[i1]


def star1(lengths):
    pos = 0
    skip_length = 0
    list_size = 256
    circle = list(range(list_size))

    for l in lengths:
        reverse(circle, pos, pos + l - 1)
        pos = (pos + l + skip_length) % list_size
        skip_length += 1

    print(circle[0]*circle[1])


def get_dense_hash(sparse):
    dense = []
    for i in range(0, 256, 16):
        sub = sparse[i:i+16]
        d = reduce((lambda a, b: a ^ b), sub)
        dense.append(d)

    return dense

def star2(lengths):
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

    print(circle)
    dense = get_dense_hash(circle)
    dense_hex = [hex(x)[2:] for x in dense]
    print("".join(dense_hex))

star1(input)
star2([ord(i) for i in inputstr])