import heapq
import sys
from collections import defaultdict
from typing import List, Tuple, Optional


die = [0]
rolls = [0]

def roll():
    rolls[0] += 1
    x = die[0]
    die[0] = (die[0] + 1) % 100
    return x + 1

def main():
    pos = [8, 3]
    scores = [0, 0]

    while True:
        for p in range(2):
            moves = roll() + roll() + roll()
            pos[p] = (pos[p] + moves) % 10
            scores[p] += pos[p] + 1

            if scores[p] >= 1000:
                print(rolls[0] * scores[(p+1)%2])
                sys.exit(0)
        

if __name__ == "__main__":
    main()
