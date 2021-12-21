import heapq
import sys
from collections import defaultdict
from typing import List, Tuple, Optional


sum_to_count = defaultdict(int)

def turn(player_is_p0, pos, scores):
    p = 0 if player_is_p0 else 1
    op = (p + 1) % 2
    if scores[op] >= 21:
        return {op: 1}
    
    to_ret = defaultdict(int)
    for moves, ways in sum_to_count.items():
        if sum(scores) == 0:
            print(moves, ways, to_ret)
        new_pos = [x for x in pos]
        new_pos[p] = (new_pos[p] + moves) % 10
        new_scores = [x for x in scores]
        new_scores[p] += new_pos[p] + 1
        res = turn(not player_is_p0, new_pos, new_scores)
        for k, v in res.items():
            to_ret[k] += ways * v
    return to_ret


def main():
    global sum_to_count
    for r1 in [1,2,3]:
        for r2 in [1,2,3]:
            for r3 in [1,2,3]:
                sum_to_count[sum((r1, r2, r3))] += 1
    print(turn(True, [8, 3], [0, 0]))

if __name__ == "__main__":
    main()
