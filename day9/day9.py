example = "{{<a!>},{<a!>},{<a!>},{<ab>}}"

def star1(input):
    group = 0
    score = 0
    garbage = False
    ignore_index = -1
    garbage_counter = 0

    for index, i in enumerate(input):
        if garbage is True:
            if ignore_index == index:
                continue
            elif i == "!":
                ignore_index = index+1
            elif i == ">":
                garbage = False
            else:
                garbage_counter += 1

        if i == "<":
            garbage = True

        if garbage is False:
            if i == "{":
                group += 1
            elif i == "}":
                score += group
                group -= 1

    print(score)
    print(garbage_counter)


with open('input.txt') as fp:
    for line in fp:
        star1(line)

star1('<{o"i!a,<{i<a>')