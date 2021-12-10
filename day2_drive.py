
def main(f):
    horiz, depth = 0, 0
    aim = 0
    for i, l in enumerate(f.readlines()):
        l = l.strip().split(" ")
        x = int(l[1])
        if l[0] == "forward":
            horiz += x
            depth += aim * x
        elif l[0] == "down":
            aim += x
        elif l[0] == "up":
            aim -= x

    print(horiz * depth)


if __name__ == "__main__":
    with open("input") as f:
        main(f)