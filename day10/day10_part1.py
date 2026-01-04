from itertools import combinations
import numpy as np
import ast

def to_indicator_np(idxs, n):
    print(idxs)
    v = np.zeros(n, dtype=int)
    if isinstance(idxs, int):
        v[idxs] = 1
    else:
        v[list(idxs)] = 1
    return v

def build_motif(n, elements):
    base = np.zeros(n, dtype=int)
    print(base)
    for element in elements:
        print(element)
        el_vec = to_indicator_np(ast.literal_eval(element), n)
        print(el_vec)
        base = (base + el_vec) %2
        print(base)
    return base



with open('day10_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    res = 0
    for line in data:
        line = line.split(' ')
        line.pop()
        motif = line.pop(0)
        chars = motif.strip()[1:-1]
        motif_v = np.fromiter((1 if c == '#' else 0 for c in chars), dtype=int)
        print(motif)
        print(motif_v)
        print(line)
        all_combos = []
        found = False
        for r in range(1, len(line) + 1):
            if found:
                break
            all_combos.extend(combinations(line, r))
            print('All combos being tested, ', all_combos)
            for combo in all_combos:
                res_motif_v = build_motif(len(motif_v), combo)
                if np.array_equal(res_motif_v, motif_v):
                    print('Found combo: ', combo)
                    res += r
                    found = True
                    break
    print(res)