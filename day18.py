def read_input(file):
    with open(file) as fp:
        return [line for line in fp]


def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


register = {}
def get_reg(reg):
    if is_number(reg):
        return int(reg)

    if reg not in register:
        register[reg] = 0

    return register[reg]


def set_reg(reg, val):
    register[reg] = val


def star1(input):
    last_played = 0
    row = 0
    while row < len(input):
        i = input[row]
        instruction = i.rstrip().split(" ")

        if instruction[0] == "snd":
            last_played = get_reg(instruction[1])
            print("snd %d" % last_played)
        elif instruction[0] == "set":
            set_reg(instruction[1], get_reg(instruction[2]))
        elif instruction[0] == "add":
            set_reg(instruction[1], get_reg(instruction[1]) + get_reg(instruction[2]))
        elif instruction[0] == "mul":
            set_reg(instruction[1], get_reg(instruction[1]) * get_reg(instruction[2]))
        elif instruction[0] == "mod":
            set_reg(instruction[1], get_reg(instruction[1]) % get_reg(instruction[2]))
        elif instruction[0] == "rcv":
            if get_reg(instruction[1]) > 0:
                print("rcv %d" % last_played)

        if instruction[0] == "jgz":
            if get_reg(instruction[1]) > 0:
                row += get_reg(instruction[2])
                continue

        row += 1


star1(read_input('day18.txt'))