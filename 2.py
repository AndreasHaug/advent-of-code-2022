def calculate1(choose: str):
    if choose[0] == "A": #rock
        match choose[2]:
            case "X": #rock 1 point
                return 1 + 3 #draw
            case "Y": #paper 2 points #win
                return 2 + 6
        return 3 + 0  #scissors 3 points lose
    elif choose[0] == "B": #paper
        match choose[2]:
            case "X": #rock 1 point
                return 1 + 0  #lose
            case "Y": #paper 2 points
                return 2 + 3 #draw
        return 3 + 6  # scissors 3 points win
    else: #scissors 3 points
        match choose[2]:
            case "X": #rock 1 point win
                return 1 + 6
            case "Y": #paper 2 points lose
                return 2 + 0
        return 3 + 3  #scissors 3 points draw

def calculate2(choose: str):
    if choose[0] == "A": #rock
        match choose[2]:
            case "X": #need to lose: scissors
                return 0 + 3
            case "Y": #need draw: rock
                return 3 + 1
        return 6 + 2 # need to win: paper
    elif choose[0] == "B": #paper
        match choose[2]:
            case "X": #need to lose: rock
                return 0 + 1
            case "Y": #need draw: paper
                return 3 + 2
        return 6 + 3 #need to win: scissors
    else: #scissors 
        match choose[2]:
            case "X": # need to lose: paper
                return 0 + 2
            case "Y": # need draw: scissors
                return 3 + 3
        return 6 + 1 # need to win: rock


def do_calculate(input_file: str, fn):
    return (sum(map(fn,
              filter(lambda x: x != "",
                     input_file.split("\n")))))

input_file = open("2.txt", "r").read()
print("Part 1: ", do_calculate(input_file, calculate1))
print("Part 2: ", do_calculate(input_file, calculate2))

