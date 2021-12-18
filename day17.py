import heapq
from typing import List, Tuple, Optional


def main(f):
    x_box = None
    y_box = None
    for i, l in enumerate(f.readlines()):
        _, _, xraw, yraw = l.strip().split()
        x_box = tuple(map(int, xraw[2:-1].split("..")))
        y_box = tuple(map(int, yraw[2:].split("..")))

    def simulate(v_x: int, v_y: int) -> Tuple[bool, int]:
        p = [0, 0]
        max_y = 0

        while True:
            p[0] += v_x
            p[1] += v_y
            max_y = max(max_y, p[1])

            # Check if it's in the box:
            in_x = x_box[0] <= p[0] <= x_box[1]
            in_y = y_box[0] <= p[1] <= y_box[1]
            if in_x and in_y:
                return True, max_y

            # Check if it can never be in the box:
            if v_x == 0 and not in_x:
                return False, 0
            if v_y <= 0 and p[1] < y_box[0]:
                return False, 0
            if v_x <= 0 and p[0] < x_box[0]:
                return False, 0
            if v_x > 0 and p[0] > x_box[1]:
                return False, 0

            # Update the velocity
            if v_x > 0:
                v_x -= 1
            elif v_x < 0:
                v_x += 1
            v_y -= 1
    initial = []
    max_y = 0
    for x in range(min(0, x_box[0]), x_box[1] + 1):
        for y in range(y_box[0], 100):
            worked, my = simulate(x, y)
            if worked:
                initial.append((x, y))
    print(len(initial))


if __name__ == "__main__":
    with open("test") as f:
        main(f)