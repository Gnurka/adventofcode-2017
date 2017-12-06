input = 361527


def get_neighboor_sum(x, y, positions):
    if x == 0 and y == 0:
        return 1

    sum = 0
    for p in positions:
        if abs(x-p[0]) <= 1 and abs(y-p[1]) <= 1:
            sum += p[2]

    return sum


def circular_coord(pos):
    x = 0
    y = 0
    dir = 3
    d = 1
    dir_counter = 1

    positions = []
    for p in range(1, pos):
        dir_counter += 1

        if dir == 0:
            y += 1
        elif dir == 1:
            x -= 1
        elif dir == 2:
            y -= 1
        elif dir == 3:
            x += 1

        if dir_counter >= d:
            dir = (dir + 1) % 4
            dir_counter = 0

            if dir == 3 or dir == 1:
                d += 1

    return x, y

def star2(pos):
    x = 0
    y = 0
    dir = 3
    d = 1
    dir_counter = 1

    positions = []
    for p in range(1, pos):
        sum = get_neighboor_sum(x, y, positions)
        positions.append((x, y, sum))
        if sum > pos:
            return sum

        dir_counter += 1

        if dir == 0:
            y += 1
        elif dir == 1:
            x -= 1
        elif dir == 2:
            y -= 1
        elif dir == 3:
            x += 1

        if dir_counter >= d:
            dir = (dir + 1) % 4
            dir_counter = 0

            if dir == 3 or dir == 1:
                d += 1

    return x, y


pos = circular_coord(361527)
print("At pos " + str(pos) + " and distance " + str(abs(pos[0]) + abs(pos[1])))

print(star2(361527))