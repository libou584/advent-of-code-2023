import re 


def is_okay(game) :
    matches = re.findall("\d{1,2}\s\w{3,5}", game)
    for match in matches :
        n = int(re.search("\d{1,2}", match).group())
        color = re.search("\w{3,5}", match).group()
        if (color == "red" and n > 12) or (color == "green" and n > 13) or (color == "blue" and n > 14) :
            return False
    return True


if __name__ == "__main__" :
    # print(is_okay("Game 1: 1 green, 2 blue; 15 blue, 12 red, 2 green; 4 red, 6 blue; 10 blue, 8 red; 3 red, 12 blue; 1 green, 12 red, 8 blue"))
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    sum = 0
    for line in lines :
        if is_okay(line) :
            sum += int(re.search("\d{1,3}", re.search("Game\s\d{1,3}", line).group()).group())
    print(sum)