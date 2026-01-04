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
    print(neighs_num)
    if neighs_num < 4:
        return 1
    else:
        return 0

with open('day4_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    grid = []
    for line in data:
        print(line)
        grid.append(list(line))
    print(grid)
    # Traverse the grid
    accessible = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            current = grid[i][j]
            print(current)
            if current == '.':
                continue
            
            acc = check_neighbours(grid, i, j)
            print(acc)
            accessible += acc

    print(accessible)