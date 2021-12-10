import sys

def main(f):
    lines = []
    numbers = []
    board_index = 0

    boards = []
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        if i == 0:
            numbers = list(map(int, l.split(",")))
            continue

        if board_index == 0:
            board_index += 1
            continue

        if board_index == 1:
            boards.append([])
        cur = boards[-1]
        cur.append([int(x) for x in l.split()])
        if len(cur) == 5:
            board_index = 0
        else:
            board_index += 1


    marked = []
    for board in boards:
        marked.append([
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ])

    scores = []
    def find_score(k, n):
        s = 0
        for i in range(5):
            for j in range(5):
                if not marked[k][i][j]:
                    s += boards[k][i][j]
        return s * n

    last_score = 0
    finished = set()
    for n in numbers:
        for k, board in enumerate(boards):
            if k in finished:
                continue

            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if col == n:
                        marked[k][i][j] = True

            # See if we got bingo in a row
            bingo = False
            for i, row in enumerate(board):
                if all(marked[k][i]):
                    bingo = True

            for j in range(5):
                if all(marked[k][i][j] for i in range(5)):
                    bingo = True

            #if all(marked[k][i][i] for i in range(5)):
            #    bingo = True

            #if all(marked[k][i][4-i] for i in range(5)):
            #    bingo = True

            if bingo:
                last_score = find_score(k, n)
                finished.add(k)

    print(last_score)


if __name__ == "__main__":
    with open("input") as f:
        main(f)