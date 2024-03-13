if __name__ == "__main__" :
    with open("input.txt", 'r') as file :
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    seeds = [int(n) for n in lines[0].split()[1:]]
    # seed_soil_map = [[int(n) for n in line.split()] for line in lines[3:50]]
    maps = [[[int(n) for n in line.split()] for line in lines[3:50]], [[int(n) for n in line.split()] for line in lines[52:80]], [[int(n) for n in line.split()] for line in lines[82:126]], [[int(n) for n in line.split()] for line in lines[128:137]], [[int(n) for n in line.split()] for line in lines[139:171]], [[int(n) for n in line.split()] for line in lines[173:209]], [[int(n) for n in line.split()] for line in lines[211:250]]]
    positions = []
    for i in range(len(seeds)) :
        seed = seeds[i]
        for map in maps :
            for (dst_start, src_start, range_length) in map :
                if seed >= src_start and seed < src_start+range_length :
                    seed = dst_start + seed - src_start
                    break
        positions.append(seed)
    print(min(positions))