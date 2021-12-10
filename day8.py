from collections import defaultdict


def main(f):
    all_sum = 0
    for i, l in enumerate(f.readlines()):
        signals, outputs = [x.strip().split() for x in l.strip().split("|")]
        m = dict()

        # First find the one that's length 3 and the one that's length 2
        seven = ''
        one = ''
        four = ''
        for s in signals:
            if len(s) == 2:
                one = s
            if len(s) == 3:
                seven = s
            if len(s) == 4:
                four = s
        top = "".join(set(seven) - set(one))

        inverse_seven = (set("abcdefg") - set(seven)) | set(top)
        for s in signals:
            if len(s) == 6 and len(set(s) - inverse_seven) == 1:
                target = "".join(set(s) - inverse_seven)
                bottom_right = target
                break

        top_right = "".join(set(one) - set(bottom_right))

        two = ''
        for s in signals:
            if len(s) != 5:
                continue
            if len(set(s) - {top_right, top}) != 3:
                continue
            if bottom_right in s:
                continue

            # Now we know this is 2.
            two = s
            top_left = "".join(set(four) - set(s) - set(bottom_right))


        five = ''
        for s in signals:
            if len(s) != 5:
                continue
            if len(set(s) - {top, top_left}) != 3:
                continue

            # We know this is a five.
            five = s
            middle_or_bottom = set(s) - {top, top_left, bottom_right}

        bottom_left = "".join(set(two) - {top, top_right} - set(five))

        zero = ''
        for s in signals:
            if len(s) != 6:
                continue
            if len(set(s) - {top, top_left, top_right, bottom_left, bottom_right}) != 1:
                continue
            zero = s

        middle = "".join(middle_or_bottom - set(zero))
        bottom = "".join(middle_or_bottom - {middle})

        cur = 0
        for o in outputs:
            n = set(o)
            v = -1
            if n == {top_right, bottom_right}:
                v = 1
            if n == {top, top_right, middle, bottom_left, bottom}:
                v = 2
            if n == {top, top_right, middle, bottom_right, bottom}:
                v = 3
            if n == {top_left, top_right, middle, bottom_right}:
                v = 4
            if n == {top, top_left, middle, bottom_right, bottom}:
                v = 5
            if n == {top, top_left, middle, bottom_left, bottom_right, bottom}:
                v = 6
            if n == {top, top_right, bottom_right}:
                v = 7
            if len(n) == 7:
                v = 8
            if n == {top, top_left, top_right, middle, bottom_right, bottom}:
                v = 9
            if n == {top, top_left, top_right, bottom_left, bottom_right, bottom}:
                v = 0
            cur = (cur * 10 + v)
        all_sum += cur

    print(all_sum)


if __name__ == "__main__":
    with open("input") as f:
        main(f)