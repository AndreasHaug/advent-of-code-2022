def get_elements(elem):
    return (list(map(int, elem[0].split("-"))),
            list(map(int, elem[1].split("-"))))


def fully_contain(elem):
    r1, r2 = get_elements(elem)
    return r2[0] <= r1[0] and r2[1] >= r1[1] or r1[0] <= r2[0] and r1[1] >= r2[1]


def overlap(elem):
    r1, r2 = get_elements(elem)
    range1 = list(range(r1[0], r1[1] + 1))
    range2 = list(range(r2[0], r2[1] + 1))
    return len(set(range1).intersection(set(range2))) > 0


def calculate(fn, input_string):
    return len(list(filter(fn, input_file)))


input_file = list(map(lambda x: x.split(","),
                      filter(lambda x: x != "",
                             open("4.txt", "r").read().split("\n"))))

print("Part 1:\t", calculate(fully_contain, input_file))
print("Part 2:\t", calculate(overlap, input_file))
