
def contains_duplicate_words(words):
    word_dict = {}
    for w in words:
        if w in word_dict:
            return True

        word_dict[w] = True


def star1():
    valid = 0
    with open('input.txt') as fp:
        for line in fp:
            words = [x for x in line.rstrip().split(' ')]

            if not contains_duplicate_words(words):
                valid += 1

        print(valid)


def contains_anagram_words(words):
    for i, w in enumerate(words):
        letters = count_letters(w)
        for j, w2 in enumerate(words):
            if i == j:
                continue

            if count_letters(w2) == letters:
                return True

    return False


def count_letters(w):
    letter_dict = {}
    for l in w:
        if l in letter_dict:
            letter_dict[l] += 1
        else:
            letter_dict[l] = 1

    return letter_dict


def star2():
    valid = 0
    with open('input.txt') as fp:
        for line in fp:
            words = [x for x in line.rstrip().split(' ')]

            if not contains_anagram_words(words):
                valid += 1

        print(valid)


input = "oiii ioii iioi iiio"
print(input + " valid=" + str(not contains_anagram_words(input.split(' '))))

star2()