grid = []

with open('day19.txt') as fp:
    for line in fp:
        grid.append([x for x in line])

r = 0
c = grid[0].index('|')
dir = 1
letters = ""
nxt = '|'
steps = 0

while nxt != ' ':
    if dir == 1 or dir == 3:
        if nxt == '+':
            if grid[r][c+1] == '-':
                dir = 0
            elif grid[r][c-1] == '-':
                dir = 2
    elif dir == 0 or dir == 2:
        if nxt == '+':
            if grid[r+1][c] == '|':
                dir = 1
            elif grid[r-1][c] == '|':
                dir = 3

    if nxt.isalpha():
        letters += nxt

    if dir == 0:
        c += 1
    elif dir == 1:
        r += 1
    elif dir == 2:
        c -= 1
    elif dir == 3:
        r -= 1

    nxt = grid[r][c]
    steps += 1

print(letters)
print(steps)

