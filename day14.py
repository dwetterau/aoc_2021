from collections import defaultdict


def main(f):
    pair_counts = defaultdict(int)
    update_map = defaultdict(list)
    template = ""
    rules = dict()
    for i, l in enumerate(f.readlines()):
        if i == 0:
            template = l.strip()
        if i < 2:
            continue
        v1, v2 = l.strip().split(" -> ")
        rules[tuple(v1)] = v2

    for rule, n in rules.items():
        update_map[rule] = [(rule[0], n), (n, rule[1])]

    for i in range(len(template)):
        if i == 0:
            continue
        pair_counts[(template[i-1], template[i])] += 1

    def extend(original):
        new_counts = defaultdict(int)
        for p, c in original.items():
            for x in update_map[p]:
                new_counts[x] += c
        return new_counts

    for i in range(40):
        pair_counts = extend(pair_counts)

    counts = defaultdict(int)
    counts[template[0]] = 1
    for x, c in pair_counts.items():
        counts[x[1]] += c
    print(max(counts.values()) - min(counts.values()))


if __name__ == "__main__":
    with open("input") as f:
        main(f)