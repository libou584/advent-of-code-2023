import re


if __name__ == "__main__" :
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    dico = {}
    for i in range(2, 760) :
        s = lines[i]
        matches = re.findall("\w{3}", s)
        dico[matches[0]] = (matches[1], matches[2])
    seq = lines[0]
    node = 'AAA'
    n = 0
    while node != 'ZZZ' :
        instruct = seq[n%len(seq)]
        if instruct == 'L' :
            node = dico[node][0]
        elif instruct == 'R' :
            node = dico[node][1]
        n += 1
    print(n)