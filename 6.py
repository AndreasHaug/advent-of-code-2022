input_file = open("6.txt", "r").read()


for a in range(0, len(input_file)):
    try:
        l = [input_file[a],
             input_file[a + 1],
             input_file[a + 2],
             input_file[a + 3] ]

        if len(set(l)) == len(l):
            print("Part 1:\t", 1 + a + 3)
            break

    except IndexError:
        pass


for a in range(0, len(input_file)):
    try:
        l = [input_file[a],
             input_file[a + 1],
             input_file[a + 2],
             input_file[a + 3],
             input_file[a + 4],
             input_file[a + 5],
             input_file[a + 6],
             input_file[a + 7],
             input_file[a + 8],
             input_file[a + 9],
             input_file[a + 10],
             input_file[a + 11],
             input_file[a + 12],
             input_file[a + 13],
             ]

        if len(set(l)) == len(l):
            print("Part 2:\t", 1 + a + 13)
            break

    except IndexError:
        pass
