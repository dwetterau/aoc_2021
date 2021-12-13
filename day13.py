from collections import defaultdict


def main(f):
    points = defaultdict(bool)
    folds = []
    for i, l in enumerate(f.readlines()):
        if l.startswith("fold along "):
            _, _, line = l.strip().split(" ")
            dir, x = line.split("=")
            folds.append((dir, int(x)))
        elif l.strip():
            v1, v2 = map(int, l.strip().split(","))
            points[(v1, v2)] = True

    for (dir, v) in folds:
        new_points = defaultdict(bool)
        if dir == "y":
            # fold along y axis
            for (x, y) in points.keys():
                if y <= v:
                    new_y = y
                else:
                    new_y = v - (y - v)
                new_points[(x, new_y)] = True
        else:
            for (x, y) in points.keys():
                if x <= v:
                    new_x = x
                else:
                    new_x = v - (x - v)
                new_points[(new_x, y)] = True
            # fold along x axis
        points = new_points

    max_x, max_y = 0, 0
    for (x, y) in points.keys():
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    for y in range(max_y+1):
        s = ""
        for x in range(max_x+1):
            s += "#" if points[(x, y)] else "."
        print(s)


if __name__ == "__main__":
    with open("input") as f:
        main(f)