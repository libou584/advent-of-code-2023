fn get1(s : String) -> Int :
    for i in range(len(s)) :
        var c : String = s[i]
        if ord(c) >= 49 and ord(c) <= 57 :
            return ord(c) - 48
    return 0


fn get2(s : String) -> Int :
    for i in range(len(s)-1, -1, -1) :
        var c : String = s[i]
        if ord(c) >= 49 and ord(c) <= 57 :
            return ord(c) - 48
    return 0


fn main() raises :
    var f = open("input.txt", "r")
    var s : String = f.read()
    var buf : String = ""
    var sum : Int = 0
    for i in range(len(s)) :
        if s[i] != '\n' :
            buf += s[i]
        else :
            sum += get1(buf)*10
            sum += get2(buf)
            buf = ""
    sum += get1(buf)*10
    sum += get2(buf)
    f.close()
    print(sum)