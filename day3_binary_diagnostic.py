
def main(f):
    lines = []
    num_bits = 0
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        lines.append(l)
        num_bits = len(l)

    candidates = lines
    out = []
    for i in range(num_bits):
        if len(candidates) == 1:
            out.append(candidates[0])
            break

        count = 0
        for l in candidates:
            b = l[i]
            if b == "1":
                count += 1

        if count >= len(candidates) / 2:
            # Include "ones"
            target = "1"
        else:
            target = "0"
        candidates = [x for x in candidates if x[i] == target]
    if len(out) == 0:
        out.append(candidates[0])

    candidates = lines
    for i in range(num_bits):
        if len(candidates) == 1:
            out.append(candidates[0])
            break

        count = 0
        for l in candidates:
            b = l[i]
            if b == "1":
                count += 1

        if count >= len(candidates) / 2:
            target = "0"
        else:
            target = "1"
        candidates = [x for x in candidates if x[i] == target]
    if len(out) == 0:
        out.append(candidates[0])

    x = 1
    for y in out:
        x *= int(y, 2)
    print(x)


if __name__ == "__main__":
    with open("input") as f:
        main(f)