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

def timer(func, *args):
    import time
    beg = time.time_ns()
    func(*args)
    end = time.time_ns()
    return end - beg

def graph(seed):
    import random
    lengths = []
    times = []
    values = {chr(i + 97): i + 1 for i in range(26)}
    for i in range(10):
        n = 50 * (i + 1)
        a = "".join(chr(random.randint(97, 122)) for _ in range(n))
        b = "".join(chr(random.randint(97, 122)) for _ in range(n))
        lengths.append(n)
        times.append(timer(hvlcs, a, b, values) / 1e6)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(lengths, times, marker="o")
    ax.grid(True)
    ax.set_title("Empirical Comparison")
    ax.set_xlabel("String Length")
    ax.set_ylabel("Time (ms)")
    fig.savefig("graph.svg")

def main():
    import optparse
    parser = optparse.OptionParser(usage="%prog [options] [file]")
    parser.add_option("--graph", action="store_true", help="graph 10 random inputs")
    parser.add_option("--seed", metavar="N", type="int", default=4533, help="seed with N instead of %default")
    opts, args = parser.parse_args()

    if opts.graph:
        return graph(opts.seed)

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
