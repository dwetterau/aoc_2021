from collections import defaultdict


def main(f):
    m = defaultdict(set)
    for i, l in enumerate(f.readlines()):
        v1, v2 = l.strip().split("-")
        m[v1].add(v2)
        m[v2].add(v1)

    def explore(path, has_double):
        top = path[-1]
        if top == "end":
            return 1

        paths = 0
        for next in m[top]:
            if next == "start":
                continue

            # Discard visiting small caves more than twice
            small = next[0].lower() == next[0]
            if small and next in path:
                if has_double:
                    continue
                new_has_double = True
            else:
                new_has_double = has_double
            paths += explore(path + [next], new_has_double)
        return paths

    print(explore(["start"], False))

if __name__ == "__main__":
    with open("input") as f:
        main(f)