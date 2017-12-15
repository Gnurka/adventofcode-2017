
def star1(start_a, start_b):
    a = start_a
    b = start_b

    matches = 0
    for i in range(40000000):
        if a & 0xFFFF == b & 0xFFFF:
            matches += 1

        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647

    return matches


def star2(a, b):
    matches = 0
    for i in range(5000000):
        a = generate(a, 16807, 4)
        b = generate(b, 48271, 8)

        if a & 0xFFFF == b & 0xFFFF:
            matches += 1

    return matches


def generate(number, factor, div):
    number = (number * factor) % 2147483647
    while number % div != 0:
        number = (number * factor) % 2147483647

    return number


#print(star1(873, 583))
print(star2(873, 583))
