from collections import defaultdict


def main(f):
    day_to_count_map = defaultdict(int)
    for i, l in enumerate(f.readlines()):
        fish = list(int(x) for x in l.strip().split(","))
        for f in fish:
            day_to_count_map[f] += 1
        break

    days = 256
    day = 0
    while day < days:
        day += 1
        new_map = defaultdict(int)
        for f, c in day_to_count_map.items():
            if f == 0:
                new_map[6] += c
                new_map[8] += c
            else:
                new_map[f-1] += c
        day_to_count_map = new_map
    print(sum(day_to_count_map.values()))

if __name__ == "__main__":
    with open("input") as f:
        main(f)