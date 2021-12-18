import heapq
import math
from typing import List, Tuple, Optional, Any


def main(f):
    def reduce(num):

        def add(num: Any, c: int, leftmost: bool) -> bool:
            if type(num) == int:
                return False
            if leftmost:
                if type(num[0]) == int:
                    num[0] += c
                    return True
                return add(num[0], c, leftmost)
            else:
                if type(num[1]) == int:
                    num[1] += c
                    return True
                return add(num[1], c, leftmost)

        def maybe_explode():
            # Returns "exploded anywhere", "left to add", "right to add", "just exploded"
            def walk(num: Any, depth: int) -> Tuple[bool, int, int, bool]:
                if type(num) == int:
                    return False, 0, 0, False

                left_exploded, left_add, right_add, just_exploded = walk(num[0], depth + 1)
                if left_exploded:
                    if just_exploded:
                        num[0] = 0
                    if right_add:
                        if not add(num[1], right_add, leftmost=True):
                            num[1] += right_add
                        right_add = 0
                    return True, left_add, right_add, False

                if depth == 4:
                    return True, num[0], num[1], True

                right_exploded, left_add, right_add, just_exploded = walk(num[1], depth + 1)
                if right_exploded:
                    if just_exploded:
                        num[1] = 0
                    if left_add:
                        if not add(num[0], left_add, leftmost=False):
                            num[0] += left_add
                        left_add = 0
                    return True, left_add, right_add, False

                return False, 0, 0, False

            exploded, _, _, _ = walk(num, 0)
            return exploded

        def maybe_split():
            def split(num: Any) -> bool:
                if type(num) == int:
                    return False
                if type(num[0]) == int:
                    if num[0] >= 10:
                        num[0] = [num[0]//2, math.ceil(num[0]/2)]
                        return True
                else:
                    if split(num[0]):
                        return True

                if type(num[1]) == int:
                    if num[1] >= 10:
                        num[1] = [num[1] // 2, math.ceil(num[1] / 2)]
                        return True
                else:
                    if split(num[1]):
                        return True
                return False
            return split(num)

        while True:
            if maybe_explode():
                continue
            if maybe_split():
                continue
            break

        return num

    number = []
    for i, l in enumerate(f.readlines()):
        next_num = eval(l.strip())
        if not number:
            number = next_num
            continue
        number = reduce([number, next_num])

    def magnitude(num):
        if type(num) == int:
            return num
        return 3*magnitude(num[0]) + 2*magnitude(num[1])
    print(number)
    print(magnitude(number))


if __name__ == "__main__":
    with open("input") as f:
        main(f)