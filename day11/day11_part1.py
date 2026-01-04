from collections import deque

with open('day11_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    links = {}
    for line in data:
        left, right = line.split(':')
        print(left)
        print(right)
        links[left] = right.split()
    print(links)
    start = deque(links['you'])
    print(start)
    paths = 0
    while start:
        curr = start.pop()
        if curr == 'out':
            print('Found an out')
            paths += 1
        else:
            for x in links[curr]:
                start.appendleft(x)
        print(start)
    print(paths)