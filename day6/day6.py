example = [0, 2, 7, 0]
input = [11, 11, 13, 7, 0, 15, 5, 5, 4,	4,	1,	1,	7,	1,	15,	11]


def find(memory, states):
    for s in states:
        if s == memory:
            return True

    return False




def find_largest(memory):
    return memory.index(max(memory))

def find_loop(memory):
    states = []
    reallocs = 0

    while not find(memory, states):
        states.append(list(memory))

        index = find_largest(memory)
        blocks = memory[index]
        memory[index] = 0
        for x in range(index+1, index+1+blocks):
            memory[x % len(memory)] += 1

        reallocs += 1

    return reallocs, memory


loop_info = find_loop(input)
print(loop_info[0])

print(find_loop(loop_info[1]))