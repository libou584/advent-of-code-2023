import re


def string2num(s) :
    x = re.search("\d$", re.search("^\w*\d", s).group()).group()
    y = re.search("^\d", re.search("\d\w*$", s).group()).group()
    return 10*int(y) + int(x)


if __name__ == "__main__" :
    # print(string2num("eriufg4ef"))
    # print(string2num("eriu2fg4ef"))
    # print(string2num("1eriu2fg4ef"))
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(sum([string2num(line) for line in lines]))