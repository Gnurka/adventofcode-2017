example = [0, 3, 0, 1, -3]


def read_instruction_file(file):
    with open(file) as fp:
        return [int(line) for line in fp]


def star1(instructions):
    index = 0
    steps = 0
    while index < len(instructions):
        jump = instructions[index]
        instructions[index] += 1
        index += jump
        steps += 1

    print(steps)


def star2(instructions):
    index = 0
    steps = 0
    while index < len(instructions):
        jump = instructions[index]

        if jump >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1

        index += jump
        steps += 1

    print(steps)


star1(read_instruction_file('input.txt'))
star2(read_instruction_file('input.txt'))