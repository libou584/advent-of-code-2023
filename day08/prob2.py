import re


def oui() :
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    dico = {}
    for i in range(2, 760) :
        s = lines[i]
        matches = re.findall("\w{3}", s)
        dico[matches[0]] = (matches[1], matches[2])
    seq = lines[0]
    return dico, seq


def finish(nodes) :
    for node in nodes :
        if node[2] != 'Z' :
            return False
    return True


if __name__ == "__main__" :
    dico, seq = oui()
    nodes = [node for node in dico.keys() if node[2] == 'A']
    n = 0
    while not finish(nodes) :
        instruct = seq[n%len(seq)]
        for i in range(len(nodes)) :
            if instruct == 'L' :
                nodes[i] = dico[nodes[i]][0]
            elif instruct == 'R' :
                nodes[i] = dico[nodes[i]][1]
        n += 1
    print(n)