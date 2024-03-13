def roll_up(M) :
    for line in range(1, len(M)) :
        for j in range(len(M[line])) :
            if M[line][j] == 'O' :
                i = line
                M[line][j] = '.'
                while i >= 0 and M[i][j] == '.' :
                    i -= 1
                M[i+1][j] = 'O'


def roll_left(M) :
    for col in range(1, len(M)) :
        for i in range(len(M)) :
            if M[i][col] == 'O' :
                j = col
                M[i][col] = '.'
                while j >= 0 and M[i][j] == '.' :
                    j -= 1
                M[i][j+1] = 'O'


def roll_down(M) :
    for line in range(len(M)-1, 0) :
        for j in range(len(M[line])) :
            if M[line][j] == 'O' :
                i = line
                M[line][j] = '.'
                while i < len(M) and M[i][j] == '.' :
                    i += 1
                M[i-1][j] = 'O'


def roll_right(M) :
    for col in range(len(M)-1, 0) :
        for i in range(len(M)) :
            if M[i][col] == 'O' :
                j = col
                M[i][col] = '.'
                while j < len(M) and M[i][j] == '.' :
                    j += 1
                M[i][j-1] = 'O'


def count(M) :
    s = 0
    for line in range(len(M)) :
        s += M[line].count('O')*(len(M) - line)
    return s



if __name__ == "__main__" : # prob2 doesn't work
    n = 1000
    f = open("sample.txt", "r")
    M = [list(line) for line in f.readlines()]
    for i in range(len(M) - 1) :
        M[i].pop()
    # print(M)
    for line in range(n) :
        roll_up(M)
        roll_left(M)
        roll_down(M)
        roll_right(M)
    # print(M)
    s = count(M)
    print(s)