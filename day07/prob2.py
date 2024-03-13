import re
from collections import Counter


dic_type = {"high" : 0, "opair" : 10, "tpair" : 20, "three" : 30, "full" : 40, "four" : 50, "five" : 60}
dic_card = {"A" : 13, "K" : 12, "Q" : 11, "J" : 0, "T" : 9, "9" : 8, "8" : 7, "7" : 6, "6" : 5, "5" : 4, "4" : 3, "3" : 2, "2" : 1}


def dico() :
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    dic = {}
    for line in lines :
        dic[line[:5]] = int(re.search("\s\d{1,4}", line).group())
    return dic


def type(hand):
    card_counts = Counter(card for card in hand if card != 'J')
    num_jokers = hand.count('J')
    if any(count + num_jokers >= 5 for count in card_counts.values()):
        return "five"
    if any(count + num_jokers >= 4 for count in card_counts.values()):
        return "four"
    if set(card_counts.values()) == {2, 3} and num_jokers >= 1:
        return "full"
    if any(count + num_jokers >= 3 for count in card_counts.values()):
        return "three"
    if list(card_counts.values()).count(2) == 2 and num_jokers >= 1:
        return "tpair"
    if list(card_counts.values()).count(2) == 1 and num_jokers >= 1:
        return "opair"
    return "high"


def is_inf(h1, h2) :
    t1, t2 = type(h1), type(h2)
    if dic_type[t1] > dic_type[t2] :
        return False
    elif dic_type[t2] > dic_type[t1] :
        return True
    for i in range(5) :
        if dic_card[h1[i]] < dic_card[h2[i]] :
            return True
        elif dic_card[h2[i]] < dic_card[h1[i]] :
            return False
    return False


def sort(liste) :
    n = len(liste)
    for _ in range(n+5) :
        for i in range(n-1) :
            if not is_inf(liste[i], liste[i+1]) :
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste


if __name__ == "__main__" :
    dic = dico()
    # print(dic)
    liste = list(dic.keys())
    liste = sort(liste)
    # for i in range(len(liste)) :
    #     print(liste[i], i+1, dic[liste[i]])
    print(sum([(i+1)*dic[liste[i]] for i in range(len(liste))]))