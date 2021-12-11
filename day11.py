from collections import defaultdict


def main(f):
    grid = defaultdict(int)
    cols = 0
    rows = 0
    for i, l in enumerate(f.readlines()):
        rows += 1
        for j, x in enumerate(int(x) for x in l.strip()):
            grid[(i, j)] = x
            cols = max(cols, j + 1)

    dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

    def next_in_range(p):
        next = []
        for d in dirs:
            r = p[0] + d[0]
            c = p[1] + d[1]
            if r < 0 or r >= rows:
                continue
            if c < 0 or c >= cols:
                continue
            next.append((r, c))
        return next

    all_flashes = 0
    steps = 10000
    for s in range(steps):
        # print("")
        # print("Step: ", s)
        # for r in range(rows):
        #    print("".join(str(grid[(r, c)]) for c in range(cols)))

        for r in range(rows):
            for c in range(cols):
                grid[(r, c)] += 1

        flashes = set()
        while True:
            last_flashes = len(flashes)
            new_grid = defaultdict(int)
            for r in range(rows):
                for c in range(cols):
                    if grid[(r, c)] > 9:
                        flashes.add((r, c))
                        for n in next_in_range((r, c)):
                            new_grid[n] += 1
                    else:
                        new_grid[(r, c)] += grid[(r, c)]
            grid = new_grid
            if len(flashes) == last_flashes:
                break
        for f in flashes:
            grid[f] = 0

        if len(flashes) == rows * cols:
            print(s + 1)
            break
        all_flashes += len(flashes)


    # print(all_flashes)


if __name__ == "__main__":
    with open("input") as f:
        main(f)