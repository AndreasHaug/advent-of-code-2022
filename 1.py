s = sorted(map(lambda x: sum(map(int, filter(lambda y: y != "", x.split("\n")))), open("1.txt", "r").read().split("\n\n")), reverse = True)

#part 1
print("Part 1:\t", s[0])

#part 2
print("Part 2:\t", sum(s[0:3]))

