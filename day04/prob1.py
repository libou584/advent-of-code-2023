import re


def nb_point(card) :
    win_nb = re.findall("\s\d{1,2}", re.search(":.*\|", card).group())
    my_nb = re.findall("\s\d{1,2}", re.search("\|.*", card).group())
    n = 0
    for nb in my_nb :
        if nb in win_nb :
            n += 1
    if n == 0 :
        return 0
    return 2**(n-1)


if __name__ == "__main__" :
    # print(nb_win("Card   1:  2 15 17 11 64 59 45 41 61 19 |  4 36 62 43 94 41 24 25 13 83 97 86 61 90 67  7 15 58 18 19 38 17 49 52 37"))
    # print(nb_point("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"))
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(sum([nb_point(line) for line in lines]))