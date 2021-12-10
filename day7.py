from collections import defaultdict


def main(f):
    pos_to_count_map = defaultdict(int)
    c = 0
    min = 1<<32
    max = 0

    for i, l in enumerate(f.readlines()):
        crabs = list(int(x) for x in l.strip().split(","))
        for f in crabs:
            c += 1
            pos_to_count_map[f] += 1
            if f < min:
                min = f
            if f > max:
                max = f
        break

    best = 1<<64
    for x in range(min, max+1):
        cost = 0
        for d, c in pos_to_count_map.items():
            n = abs(d - x)
            triangle = (n * (n + 1)) / 2

            cost += triangle * c
        if cost < best:
            best = int(cost)

    print(best)


if __name__ == "__main__":
    with open("input") as f:
        main(f)