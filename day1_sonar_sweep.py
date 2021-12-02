
def main(f):
    last = 1<<32
    sums = [0, 0, 0]
    increases = 0
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        this = int(l)

        sums = [x + this for x in sums]
        if i >= 2:
            if sums[-1] > last:
                increases += 1
            last = sums[-1]
        j = len(sums) - 1
        while j > 0:
            sums[j] = sums[j-1]
            j -= 1
        sums[0] = 0

    print(increases)


if __name__ == "__main__":
    with open("input") as f:
        main(f)