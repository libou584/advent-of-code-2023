import re 


def power(game) :
    matches = re.findall("\d{1,2}\s\w{3,5}", game)
    red, green, blue = 0, 0, 0
    for match in matches :
        n = int(re.search("\d{1,2}", match).group())
        color = re.search("\w{3,5}", match).group()
        if color == "red" :
            red = max(red, n)
        elif color == "green" :
            green = max(green, n)
        elif color == "blue" :
            blue = max(blue, n)
    return red*blue*green


if __name__ == "__main__" :
    # print(power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    sum = 0
    for line in lines :
        sum += power(line)
    print(sum)