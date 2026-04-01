#!/usr/bin/env python3

import sys

zero = (0, "")

def hvlcs(a, b, values):
    m = [[None for _ in b] for _ in a]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if ai == bj:
                v, x = m[i - 1][j - 1] if i and j else zero
                m[i][j] = v + values[ai], x + ai
            else:
                mi = m[i - 1][j] if i else zero
                mj = m[i][j - 1] if j else zero
                m[i][j] = mi if mi[0] > mj[0] else mj
    return m[-1][-1]

def main():
    import optparse
    parser = optparse.OptionParser(usage="%prog [options] [file]")
    opts, args = parser.parse_args()

    if args:
        sys.stdin.close()
        sys.stdin = open(args[0])

    k = int(next(sys.stdin))
    values = {}

    for i in range(k):
        c, v = next(sys.stdin).split()
        values[c] = int(v)

    a = next(sys.stdin).strip()
    b = next(sys.stdin).strip()

    val, seq = hvlcs(a, b, values)
    print(val)
    print(seq)

if __name__ == "__main__":
    main()
