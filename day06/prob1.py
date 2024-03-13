races = [(59, 543), (68, 1020), (82, 1664), (74, 1022)]


def winning(race, hold_time) :
    time, record = race
    distance = hold_time*(time - hold_time)
    return distance > record


if __name__ == "__main__" :
    n = 1
    for race in races :
        m = 0
        time = race[0]
        for hold_time in range(1, time) :
            if winning(race, hold_time) :
                m += 1
        n *= m 
    print(n)