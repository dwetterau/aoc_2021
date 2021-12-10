def main(f):
    bad_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    good_scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []
    for i, l in enumerate(f.readlines()):
        s = []
        corrupt = False
        for c in l.strip():
            if c in "([{<":
                if c == "(":
                    s.append(")")
                if c == "[":
                    s.append("]")
                if c == "{":
                    s.append("}")
                if c == "<":
                    s.append(">")
                continue
            if len(s) == 0 or c != s[-1]:
                # corrupt, so ignore it.
                corrupt = True
                break
            s.pop()
        if corrupt:
            continue

        check = ""
        cur = 0
        while s:
            n = s.pop()
            check += n
            cur = 5 * cur + good_scores[n]
        scores.append(cur)

    scores.sort()
    print(scores[len(scores)//2])

if __name__ == "__main__":
    with open("input") as f:
        main(f)