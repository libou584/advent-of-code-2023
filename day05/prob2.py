def in_seeds(seed) :
    seed_list = [1263068588, 44436703, 1116624626, 2393304, 2098781025, 128251971, 2946842531, 102775703, 2361566863, 262106125, 221434439, 24088025, 1368516778, 69719147, 3326254382, 101094138, 1576631370, 357411492, 3713929839, 154258863]
    for i in range(len(seed_list)//2) :
        if seed >= seed_list[2*i] and seed < seed_list[2*i] + seed_list[2*i + 1] :
            return True
    return False


def antecedent(n, map) :
    for (dst_start, src_start, range_length) in map :
        if n >= dst_start and n < dst_start+range_length :
            return src_start + n - dst_start
    return n


if __name__ == "__main__" :
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    maps = [[[int(n) for n in line.split()] for line in lines[3:50]], [[int(n) for n in line.split()] for line in lines[52:80]], [[int(n) for n in line.split()] for line in lines[82:126]], [[int(n) for n in line.split()] for line in lines[128:137]], [[int(n) for n in line.split()] for line in lines[139:171]], [[int(n) for n in line.split()] for line in lines[173:209]], [[int(n) for n in line.split()] for line in lines[211:250]]]
    n = 0
    while True :
        # if n%100000 == 0 :
        #     print(n)
        s = n
        for map in maps[::-1] :
            s = antecedent(s, map)
        if in_seeds(s) :
            break
        else :
            n += 1
    print(n)