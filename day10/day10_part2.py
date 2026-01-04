#build step by step using recursion, breaking if we go over on any
import ast
import numpy as np
from scipy.optimize import linprog

def to_indicator_np(idxs, n):
    v = np.zeros(n, dtype=int)
    if isinstance(idxs, int):
        v[idxs] = 1
    else:
        v[list(idxs)] = 1
    return v

with open('day10_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    final_res = 0
    for line in data:
        line = line.split(' ')
        line.pop(0)
        joltage_target = np.array(list(map(int, line.pop().strip()[1:-1].split(','))))
        print(joltage_target)
        print(joltage_target.shape)
        print(line)
        print(len(line))
        n = len(joltage_target)
        matrix = np.array([to_indicator_np(ast.literal_eval(el), n) for el in line]).T
        c = np.ones(len(line))
        print(matrix)
        print(matrix.shape)
        res = linprog(c, A_eq=matrix, b_eq=joltage_target, integrality=1)
        print(res.x)
        final_res += res.x.sum()
    print(final_res)