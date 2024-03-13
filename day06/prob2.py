race = (59688274, 543102016641022)


def winning(race, hold_time) :
    time, record = race
    distance = hold_time*(time - hold_time)
    return distance > record


if __name__ == "__main__" :
    m = 0
    time = race[0]
    for hold_time in range(1, time) :
        if winning(race, hold_time) :
            m += 1
    print(m)