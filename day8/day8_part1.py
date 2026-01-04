# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "numpy",
# ]
# ///

import numpy as np
from collections import Counter

def smallest_edges_bruteforce(A, N):
    A = np.asarray(A, dtype=float)
    print('A: ', A)
    n = len(A)
    diff = A[:, None, :] - A[None, :, :]
    print('diff: ', diff)
    D = np.linalg.norm(diff, axis=2)
    print('D: ', D)
    iu, ju = np.triu_indices(n, k=1)
    print('iu: ', iu)
    print('ju: ', ju)
    pair_dists = D[iu, ju]
    print('pair_dists: ', pair_dists)
    N = min(N, pair_dists.size)
    print('N: ', N)
    sel = np.argpartition(pair_dists, N - 1)[:N]
    print('sel: ', sel)
    sel_sorted = sel[np.argsort(pair_dists[sel])]
    print('sel_sorted: ', sel_sorted)
    edges = list(zip(iu[sel_sorted], ju[sel_sorted], pair_dists[sel_sorted]))
    return edges

num_of_groups = 10
with open('day8_test.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    A = [tuple(map(int, row.split(','))) for row in data]
    print(A)
    edges = smallest_edges_bruteforce(A, num_of_groups)
    edges_with_points = [(A[edge[0]], A[edge[1]], edge[2]) for edge in edges]
    print(edges_with_points)
    
    # Union-Find: groups[i] points to parent, root is when groups[i] == i
    groups = [i for i in range(len(A))]
    
    def find(x):
        """Find root of x, with path compression"""
        if groups[x] != x:
            groups[x] = find(groups[x])
        return groups[x]
    
    def union(x, y):
        """Union two groups, keeping smallest as root"""
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return  # already in same group
        # Merge to smallest root
        if root_x < root_y:
            groups[root_y] = root_x
        else:
            groups[root_x] = root_y
    
    for edge in edges:
        point1_idx, point2_idx = edge[0], edge[1]
        union(point1_idx, point2_idx)
        print(groups)
    
    # Flatten all paths to roots
    for i in range(len(A)):
        find(i)
        
    print(groups)
    group_counts = Counter(groups)
    print(group_counts)
    sum_3_largest = sorted(group_counts.values(), reverse=True)[:3]
    res_mult = np.prod(sum_3_largest)
    print(res_mult)