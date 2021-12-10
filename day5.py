from collections import defaultdict


def main(f):
    points = defaultdict(int)
    for i, l in enumerate(f.readlines()):
        l = l.strip().split()
        start = tuple(map(int, l[0].split(",")))
        end = tuple(map(int, l[2].split(",")))

        cur = start

        dir_x = (end[0] - cur[0])
        dir_y = (end[1] - cur[1])

        delta = (clamp(dir_x), clamp(dir_y))
        points[cur] += 1
        while True:
            cur = tuple(cur[i] + delta[i] for i in range(len(cur)))
            points[cur] += 1
            if cur == end:
                break

    print(sum(1 for v in points.values() if v >= 2))


def clamp(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


if __name__ == "__main__":
    with open("input") as f:
        main(f)