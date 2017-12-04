from math import sqrt

input = 361527

def closest_odd_integer(number):
    rounded = round(number)
    if rounded%2!=0:
        return rounded
    else:
        return rounded-1

def circular_coord(pos):
    prev_d = closest_odd_integer(sqrt(pos))
    rest = pos - prev_d * prev_d
    d = prev_d + 2


def circular_coord_2(pos):
    x = 1
    y = 0
    dir = 0
    d = 3
    dir_counter = 0
    for p in range(2, pos):
        dir_counter += 1

        if dir == 0:
            y += 1
        elif dir == 1:
            x -= 1
        elif dir == 2:
            y -= 1
        elif dir == 3:
            x += 1

        if dir_counter >= d-1:
            dir = (dir + 1) % 4
            dir_counter = 0

    return (x, y)

print(circular_coord_2(9))