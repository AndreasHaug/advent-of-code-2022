s = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = dict(map(lambda x: (s[x], x), range(len(s))))
    
def common_char(c1: str, c2: str):
    for c in c1:
        if c in c2:
            return priorities[c]

def common_3_char(c1, c2, c3):
    for c in c1:
        if c in c2 and c in c3:
            return priorities[c]

def calc_str(string):
    c1 = string[0:(int(len(string) / 2))]
    c2 = string[(int(len(string) / 2)):(int(len(string)))]    
    return common_char(c1, c2)

input_file = list(filter(lambda x: x != "", open("3.txt", "r").read().split("\n")))

print("Part 1:\t", sum(map(calc_str, input_file)))
print("Part 2:\t", sum(map(lambda x: common_3_char(input_file[x],
                                              input_file[x + 1],
                                              input_file[x + 2]),
                           range(0, len(input_file), 3))))
