import heapq
from collections import defaultdict
from typing import List, Tuple, Optional


def main(f):
    alg = dict()
    grid = defaultdict(bool)
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        if i == 0:
            alg = {i: l[i] == "#" for i in range(len(l))}
            continue
        if i == 1:
            continue
        for j in range(len(l)):
            grid[(i-2, j)] = l[j] == "#"

    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    def enhance(grid, inf_is_set=False):
        min_r = min(r for (r, _) in grid.keys())
        max_r = max(r for (r, _) in grid.keys())
        min_c = min(c for (_, c) in grid.keys())
        max_c = max(c for (_, c) in grid.keys())
        new_grid = defaultdict(bool)
        for r in range(min_r-1, max_r + 2):
            for c in range(min_c-1, max_c + 2):
                i = 0
                for (ro, co) in offsets:
                    nr = r + ro
                    nc = c + co
                    is_set = inf_is_set
                    if (nr, nc) in grid:
                        is_set = grid[(nr, nc)]
                    i = (i << 1) | (1 if is_set else 0)
                new_grid[(r, c)] = alg[i]
        if alg[0]:
            if not inf_is_set:
                inf_is_set = True
                return new_grid, inf_is_set
        if inf_is_set:
            if not alg[511]:
                inf_is_set = False
        return new_grid, inf_is_set

    def print_grid(grid):
        min_r = min(r for (r, _) in grid.keys())
        max_r = max(r for (r, _) in grid.keys())
        min_c = min(c for (_, c) in grid.keys())
        max_c = max(c for (_, c) in grid.keys())
        for r in range(min_r, max_r + 1):
            if r == min_r:
                print("Grid ({},{}) - ({},{})", min_r, max_r, min_c, max_c)
            row = ""
            for c in range(min_c, max_c + 1):
                row += "#" if grid[(r, c)] else "."
            print(row)

    inf = False
    for times in range(50):
        grid, inf = enhance(grid, inf)
    print(sum(1 for x in grid.values() if x))


if __name__ == "__main__":
    with open("input") as f:
        main(f)