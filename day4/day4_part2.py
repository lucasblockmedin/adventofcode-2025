def check_neighbours(grid, i, j):
    neighs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighs_num = 0
    for neigh in neighs:
        new_i = i + neigh[0]
        new_j = j + neigh[1]
        if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
            continue
        if grid[new_i][new_j] == '@':
            neighs_num += 1
    # print(neighs_num)
    if neighs_num < 4:
        return True
    else:
        return False

def pretty_print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

with open('day4_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    # print(data)
    grid = []
    for line in data:
        print(line)
        grid.append(list(line))
    # print(grid)
    i = 0
    accessible_overall = 0
    accessible_now = 0
    while i < len(grid):
        # print('Grid')
        # pretty_print_grid(grid)
        # print(accessible_now)
        for j in range(len(grid[0])):
            current = grid[i][j]
            # print(current)
            if current == '.':
                continue
            
            if check_neighbours(grid, i, j):
                accessible_now += 1
                grid[i][j] = '.'
        if accessible_now > 0:
            i = -1
            accessible_overall += accessible_now
            accessible_now = 0
        i += 1
    print(accessible_overall)