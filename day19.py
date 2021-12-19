import heapq
import math
from collections import defaultdict
from typing import List, Tuple, Optional, Any

class Scanner:
    def __init__(self, beacons):
        self.beacons = beacons
        self.is_set = False

    def set(self, base, o):
        self.beacons = [
            [p[x] + base[x] for x in range(len(p))]
            for p in self.orientation(o)
        ]
        self.is_set = True
        self.loc = base

    def orientation(self, n):
        to_return = []
        for (x, y, z) in self.beacons:
            if n < 4:
                # -z
                pass
            if 4 <= n < 8:
                # z
                x, y, z = -x, y, -z
            if 8 <= n < 12:
                # -y
                x, y, z = -x, z, y
            if 12 <= n < 16:
                # y
                x, y, z = x, z, -y
            if 16 <= n < 20:
                # x
                x, z = -z, x
            if 20 <= n < 24:
                # -x
                x, z = z, -x
            if n % 2 == 1:
                y, x = x, y
            if n % 4 in (1, 2):
                y = -y
            if n % 4 in (2, 3):
                x = -x
            to_return.append([x, y, z])
        return to_return


def main(f):
    scanners = []
    cur = []
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        if l.startswith("---"):
            if cur:
                scanners.append(Scanner(cur))
            cur = []
            continue
        if not l:
            continue
        cur.append(list(map(int, l.split(","))))
    scanners.append(Scanner(cur))
    scanners[0].is_set = True
    scanners[0].loc = (0, 0, 0)

    some_unset = True
    while some_unset:
        some_unset = False
        for i, scanner_1 in enumerate(scanners):
            if not scanner_1.is_set:
                continue
            sorted_points = sorted(scanner_1.beacons)
            for j, scanner_2 in enumerate(scanners):
                if i == j:
                    continue
                if scanner_2.is_set:
                    continue
                some_unset = True

                for o in range(24):
                    points = scanner_2.orientation(o)

                    matches = defaultdict(int)
                    for p1 in sorted_points:
                        for p in points:
                            t = tuple(p1[x] - p[x] for x in range(3))
                            matches[t] += 1

                    for offset, count in matches.items():
                        if count >= 12:
                            print("Setting scanner", j, offset, o)
                            scanner_2.set(offset, o)
                            break
                    if scanner_2.is_set:
                        break
    """
    points = set()
    for s in scanners:
        for p in s.beacons:
            points.add(tuple(p))
    print(len(points))
    """
    m = 0
    for i, s1 in enumerate(scanners):
        for j in range(i, len(scanners)):
            p1 = s1.loc
            p2 = scanners[j].loc
            m = max(sum(abs(p1[x] - p2[x]) for x in range(len(p1))), m)
    print(m)


if __name__ == "__main__":
    with open("input") as f:
        main(f)