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
    n = len(A)
    diff = A[:, None, :] - A[None, :, :]
    D = np.linalg.norm(diff, axis=2)
    iu, ju = np.triu_indices(n, k=1)
    pair_dists = D[iu, ju]
    N = min(N, pair_dists.size)
    sel = np.argpartition(pair_dists, N - 1)[:N]
    sel_sorted = sel[np.argsort(pair_dists[sel])]
    edges = list(zip(iu[sel_sorted], ju[sel_sorted], pair_dists[sel_sorted]))
    return edges

def create_groups_given_N(A, N):
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
    edges = smallest_edges_bruteforce(A, N)
    groups = [i for i in range(len(A))]
    for edge in edges:
        point1_idx, point2_idx = edge[0], edge[1]
        union(point1_idx, point2_idx)

        roots = [find(i) for i in range(len(A))]
        if len(Counter(roots).values()) == 1:
            print('1 group')
            print('N: ', N)
            print('Product of X in both nodes: ', A[point1_idx][0] * A[point2_idx][0])
            #Print the last link that was created
            
            break
    return groups

with open('day8_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    A = [tuple(map(int, row.split(','))) for row in data]
    # Iterate over N until groups is just one
    print('Upper bound: ', (len(A)*(len(A)-1)//2))
    N = (len(A)*(len(A)-1)//2)
    groups = create_groups_given_N(A, N)
    if len(Counter(groups).values()) == 1:
        print('1 group')
        #Print the last link that was created
        print('last link with points: ', A[smallest_edges_bruteforce(A, N)[-1][0]], A[smallest_edges_bruteforce(A, N)[-1][1]], smallest_edges_bruteforce(A, N)[-1][2])