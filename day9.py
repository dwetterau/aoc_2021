from collections import defaultdict


def main(f):
    heat = []
    for i, l in enumerate(f.readlines()):
        line = list(int(x) for x in l.strip())
        heat.append(line)

    points_to_basin = {}
    basin_to_points = {}
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def next_in_range(p):
        next = []
        for d in dirs:
            r = p[0] + d[0]
            c = p[1] + d[1]
            if r < 0 or r >= len(heat):
                continue
            if c < 0 or c >= len(heat[r]):
                continue
            next.append((r, c))
        return next


    for row in range(len(heat)):
        for col in range(len(heat[row])):
            v = heat[row][col]
            p = (row, col)

            low = True
            for np in next_in_range(p):
                if heat[np[0]][np[1]] < v:
                    low = False
                    break
            if not low:
                continue

            new_basin_num = len(basin_to_points)
            points_to_basin[p] = new_basin_num
            basin_to_points[new_basin_num] = {p}
            frontier = [p]
            while frontier:
                next_frontier = []
                for p in frontier:
                    v = heat[p[0]][p[1]]
                    for np in next_in_range(p):
                        nv = heat[np[0]][np[1]]
                        # Does this need to compare to v?
                        if nv == 9 or nv < v:
                            continue
                        if np in points_to_basin:
                            # Does we merge basins?
                            continue
                        basin_to_points[new_basin_num].add(np)
                        points_to_basin[np] = new_basin_num
                        next_frontier.append(np)
                frontier = next_frontier

    sizes = [len(v) for v in basin_to_points.values()]
    sizes.sort(reverse=True)
    p = 1
    for x in sizes[:3]:
        p *= x
    print(p)


if __name__ == "__main__":
    with open("input") as f:
        main(f)