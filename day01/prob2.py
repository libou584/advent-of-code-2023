import re

nums = {"one" : "1" , "two" : "2" , "three" : "3" , "four" : "4" , "five" : "5" , "six" : "6" , "seven" : "7" , "eight" : "8" , "nine" : "9"}

def parse_string(s) :
    new_s = ""
    i = 0
    n = len(s)
    while i < n :
        if s[i] in nums.values() :
            new_s = new_s + s[i]
            i += 1
        else :
            b = False
            for digit in nums.keys() :
                m = len(digit)
                if n-i >= m and s[i:i+m] == digit :
                    new_s = new_s + nums[digit]
                    i += 1 #########
                    b = True
                    break
            if not b :
                i += 1
    return new_s


# def ultimate_parse(s) :
#     matches = re.findall("(one|two|three|four|five|six|seven|eight|nine|\d)", s)
#     x = int(nums[matches[0]]) if matches[0] in nums.keys() else int(matches[0])
#     y = int(nums[matches[-1]]) if matches[-1] in nums.keys() else int(matches[-1])
#     return 10*x + y


if __name__ == "__main__" :
    # print(ultimate_parse("oneight"))
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    sum = 0
    for line in lines :
        s = parse_string(line)
        sum += 10*int(s[0]) + int(s[-1])
    print(sum)
    # for line in lines :
    #     sum += ultimate_parse(line)
    # print(sum)