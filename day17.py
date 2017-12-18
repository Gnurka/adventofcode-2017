from time import time


def star1(steps, insertions):
    buffer = [0]
    pos = 0

    for i in range(1, insertions+1):
        pos = (pos+steps) % len(buffer)+1
        buffer.insert(pos, i)

        if i % 1000000 == 0:
            print(i)

    print(buffer[pos+1])
    print(buffer)


star1(3, 2017)
star1(324, 2017)

star1(324, 50000000)

def star2(steps, insertions):
    #buffer = [0]
    length = 1
    pos = 0
    val_pos1 = 0

    for i in range(1, insertions+1):
        pos = (pos+steps) % length+1

        if pos == 1:
            val_pos1 = i

        length += 1

        if i % 1000000 == 0:
            print(i, val_pos1)

    print(val_pos1)

star2(324, 50000000)
