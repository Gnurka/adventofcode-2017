from collections import deque


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


#star1(read_input('day18.txt'))


class Program:

    def __init__(self, input, regs):
        self.input = input
        self.registers = regs
        self.queue = deque()
        self.row = 0
        self.sends = 0
        self.other_program = None
        self.is_waiting = False

    def exec(self):
        while self.row < len(self.input):
            i = self.input[self.row]
            instruction = i.rstrip().split(" ")

            if instruction[0] == "snd":
                val = self.get_reg(instruction[1])
                self.other_program.queue.append(val)
                self.sends += 1
                #print("snd %d" % last_played)
            elif instruction[0] == "set":
                self.set_reg(instruction[1], self.get_reg(instruction[2]))
            elif instruction[0] == "add":
                self.set_reg(instruction[1], self.get_reg(instruction[1]) + self.get_reg(instruction[2]))
            elif instruction[0] == "mul":
                self.set_reg(instruction[1], self.get_reg(instruction[1]) * self.get_reg(instruction[2]))
            elif instruction[0] == "mod":
                self.set_reg(instruction[1], self.get_reg(instruction[1]) % self.get_reg(instruction[2]))
            elif instruction[0] == "rcv":
                if len(self.queue) > 0:
                    val = self.queue.popleft()
                    self.set_reg(instruction[1], val)
                    self.is_waiting = False
                    #print("rcv %s:%d" % (snd[0], snd[1]))
                else:
                    self.is_waiting = True
                    return

            if instruction[0] == "jgz":
                if self.get_reg(instruction[1]) > 0:
                    self.row += self.get_reg(instruction[2])
                    continue

            self.row += 1


    def is_alive(self):
        return self.row >= 0 and self.row < len(self.input)


    def get_reg(self, reg):
        if is_number(reg):
            return int(reg)

        if reg not in self.registers:
            self.registers[reg] = 0

        return self.registers[reg]

    def set_reg(self, reg, val):
        self.registers[reg] = val


def star2(input):
    p0 = Program(input, {'p': 0})
    p1 = Program(input, {'p': 1})
    p0.other_program = p1
    p1.other_program = p0

    while p0.is_alive() and p1.is_alive():
        if p0.is_alive():
            p0.exec()

        if p1.is_alive():
            p1.exec()

        if p0.is_waiting and len(p0.queue) == 0 and p1.is_waiting and len(p1.queue) == 0:
            break

    print(p0.sends)
    print(p1.sends)



star2(read_input('day18.txt'))