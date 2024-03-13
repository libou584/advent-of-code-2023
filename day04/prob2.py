import re


def nb_match(card) :
    win_nb = re.findall("\s\d{1,2}", re.search(":.*\|", card).group())
    my_nb = re.findall("\s\d{1,2}", re.search("\|.*", card).group())
    n = 0
    for nb in my_nb :
        if nb in win_nb :
            n += 1
    return n


def total_card() :
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    liste = [1 for line in lines]
    for i in range(len(liste)) :
        n = liste[i]
        n_match = nb_match(lines[i])
        for j in range(1, n_match+1) :
            liste[i+j] += n
    return sum(liste)


if __name__ == "__main__" :
    print(total_card())