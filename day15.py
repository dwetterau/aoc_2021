import heapq


def main(f):
    grid = []
    cols = 0
    rows = 0
    for i, l in enumerate(f.readlines()):
        rows += 1
        row = []
        for j, x in enumerate(int(x) for x in l.strip()):
            row.append(x)
            cols = max(cols, j + 1)
        grid.append(row)

    tiles = 5
    min_danger = []
    for r in range(rows* tiles):
        min_danger.append([0 for c in range(cols * tiles)])
    min_danger[0][0] = 0

    real_grid = []
    for r in range(rows * tiles):
        real_row = []
        for c in range(cols * tiles):
            if r == 0 and c == 0:
                real_row.append(grid[0][0])
                continue
            orig_v = grid[r % rows][c % cols]
            v = ((orig_v + (r // rows) + (c // cols) - 1) % 9) + 1
            real_row.append(v)
        real_grid.append(real_row)

    dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    visited = {(0, 0): True}
    queue = [(0, 0, 0)]
    heapq.heapify(queue)
    while True:
        cost, r, c = heapq.heappop(queue)
        if (r, c) == (rows * tiles - 1, cols * tiles - 1):
            print(cost)
            break
        for d in dirs:
            n = (r + d[0], c + d[1])
            if n[0] < 0 or n[0] >= rows * tiles or n[1] < 0 or n[1] >= cols * tiles:
                continue
            if n not in visited:
                heapq.heappush(queue, (cost + real_grid[n[0]][n[1]], n[0], n[1]))
                visited[n] = True


if __name__ == "__main__":
    with open("input") as f:
        main(f)