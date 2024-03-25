def roll_up(M) :
    for line in range(1, len(M)) :
        for j in range(len(M[line])) :
            if M[line][j] == 'O' :
                i = line
                M[line][j] = '.'
                while i >= 0 and M[i][j] == '.' :
                    i -= 1
                M[i+1][j] = 'O'
    return M


def roll_left(M) :
    for col in range(1, len(M[0])) :
        for i in range(len(M)) :
            if M[i][col] == 'O' :
                j = col
                M[i][col] = '.'
                while j >= 0 and M[i][j] == '.' :
                    j -= 1
                M[i][j+1] = 'O'
    return M


def roll_down(M) :
    for line in range(len(M)-2, -1, -1) :
        for j in range(len(M[line])) :
            if M[line][j] == 'O' :
                i = line
                M[line][j] = '.'
                while i < len(M) and M[i][j] == '.' :
                    i += 1
                M[i-1][j] = 'O'
    return M


def roll_right(M) :
    for col in range(len(M[0])-2,-1, -1) :
        for i in range(len(M)) :
            if M[i][col] == 'O' :
                j = col
                M[i][col] = '.'
                while j < len(M) and M[i][j] == '.' :
                    j += 1
                M[i][j-1] = 'O'
    return M


def count(M) :
    s = 0
    for line in range(len(M)) :
        s += M[line].count('O')*(len(M) - line)
    return s


def printM(M) :
    for line in M :
        print(line)



if __name__ == "__main__" : # prob2 doesn't work
    n = 100000
    f = open("input.txt", "r")
    M = [list(line) for line in f.readlines()]
    for i in range(len(M) - 1) :
        M[i].pop()
    # printM(M)
    # print('')
    for i in range(n) :
        M = roll_up(M)
        # printM(M)
        # print(count(M))
        M = roll_left(M)
        # printM(M)
        # print(count(M))
        M = roll_down(M)
        # printM(M)
        # print(count(M))
        M = roll_right(M)
        # printM(M)
        print(i+1, ' ', count(M))
    # print(M)
    s = count(M)
    print(s)