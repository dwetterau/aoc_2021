import heapq
from typing import List, Tuple, Optional


def main(f):
    hex_s = ""
    for i, l in enumerate(f.readlines()):
        hex_s = l.strip()

    to_parse = ''
    for h in hex_s:
        to_parse += {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111",
        }[h]

    def parse_packet(s: str, num_to_parse: Optional[int]=None) -> Tuple[str, List[int]]:
        parsed = 0
        vals = []
        while s:
            if all(x == "0" for x in s):
                break
            packet_version = int(s[:3], 2)
            s = s[3:]
            type_id = int(s[:3], 2)
            s = s[3:]

            if type_id == 4:
                # Parse literal values
                v = ""
                while True:
                    continuation = s[:1]
                    s = s[1:]
                    v += s[:4]
                    s = s[4:]
                    if continuation == "0":
                        break
                vals.append(int(v, 2))
            else:
                # This is an operator packet
                mode = s[:1]
                s = s[1:]
                if mode == "0":
                    l = int(s[:15], 2)
                    s = s[15:]
                    _, inner_vals = parse_packet(s[:l])
                    s = s[l:]
                else:
                    l = int(s[:11], 2)
                    s = s[11:]
                    s, inner_vals = parse_packet(s, l)

                if type_id == 0:
                    vals.append(sum(inner_vals))
                elif type_id == 1:
                    x = 1
                    for v in inner_vals:
                        x *= v
                    vals.append(x)
                elif type_id == 2:
                    vals.append(min(inner_vals))
                elif type_id == 3:
                    vals.append(max(inner_vals))
                elif type_id == 5:
                    assert len(inner_vals) == 2
                    vals.append(1 if inner_vals[0] > inner_vals[1] else 0)
                elif type_id == 6:
                    assert len(inner_vals) == 2
                    vals.append(1 if inner_vals[0] < inner_vals[1] else 0)
                elif type_id == 7:
                    assert len(inner_vals) == 2
                    vals.append(1 if inner_vals[0] == inner_vals[1] else 0)

            parsed += 1
            if num_to_parse and parsed == num_to_parse:
                break
        return s, vals

    print(parse_packet(to_parse))


if __name__ == "__main__":
    with open("input") as f:
        main(f)