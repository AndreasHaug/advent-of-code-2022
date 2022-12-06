def build_crates(first):
    l = [[], [], [], [], [], [], [], [], [], []]

    for a in range(0, len(first) - 1):
        s = " "
        for b in range(1, 35, 4):
            s += first[a][b]

        for c in range(len(s)):
            if (s[c] != " "):
                l[c].append(s[c])
    return l


def get_moves(line):
    numbers = line
    numbers = numbers.replace("move ", "")
    numbers = numbers.replace(" from ", " ")
    numbers = numbers.replace(" to ", " ")
    numbers = list(map(int, filter(str.isdigit, numbers.split(" "))))
    return numbers


def get_result(l):
    res = ""
    for a in range(1, len(l)):
        res += l[a][0]
    return res


def move(first, second, fn):
    l = build_crates(first)
    for a in second:
        l = fn(l, a)
    return get_result(l)


def fn_1(l, elem):
    numbers = get_moves(elem)
    for m in range(0, numbers[0]):
        move = l[numbers[1]].pop(0)
        l[numbers[2]].insert(0, move)    
    return l


def fn_2(l, elem):
    numbers = get_moves(elem)
    t = []
    for m in range(0, numbers[0]):
        t.append(l[numbers[1]].pop(0))
    l[numbers[2]] = t + l[numbers[2]]
    return l

    
input_file = list(open("5.txt", "r").read().split("\n\n"))
first = input_file[0].split("\n")
second = list(filter(lambda x: x != "", input_file[1].split("\n")))

print("Part 1:", move(first, second, fn_1))
print("Part 2:", move(first, second, fn_2))        
