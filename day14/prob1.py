def roll_up(M, line) :
    for j in range(len(M[line])) :
        if M[line][j] == 'O' :
            i = line
            M[line][j] = '.'
            while i >= 0 and M[i][j] == '.' :
                i -= 1
            M[i+1][j] = 'O'
    return M


def count(M) :
    s = 0
    for line in range(len(M)) :
        s += M[line].count('O')*(len(M) - line)
    return s



if __name__ == "__main__" :
    f = open("input.txt", "r")
    M = [list(line) for line in f.readlines()]
    for i in range(len(M) - 1) :
        M[i].pop()
    # print(M)
    for line in range(1, len(M)) :
        M = roll_up(M, line)
    # print(M)
    s = count(M)
    print(s)