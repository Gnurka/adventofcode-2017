max_reg = 0
with open('input.txt') as fp:
    regs = {}
    for line in fp:
        i = line.split(' ')
        if i[0] not in regs:
            regs[i[0]] = 0

        if i[4] not in regs:
            regs[i[4]] = 0

        cmp = i[5]

        a = regs[i[4]]
        b = int(i[6])
        condition = cmp == "<" and a < b or cmp == "<=" and a <= b or cmp == ">" and a > b or cmp == ">=" and a >= b or cmp == "==" and a == b or cmp == "!=" and a != b
        if condition is True:
            if i[1] == "inc":
                regs[i[0]] += int(i[2])
            elif i[1] == "dec":
                regs[i[0]] -= int(i[2])

        newMax = max(regs.values())
        if newMax > max_reg:
            max_reg = newMax

print(max_reg)