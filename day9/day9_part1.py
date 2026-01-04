from itertools import combinations

with open('day9_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    pairs = list(combinations(data, 2))
    max_area = 0
    for left, right in pairs:
        left_x, left_y = left.split(',')
        right_x, right_y = right.split(',')
        left_x, left_y, right_x, right_y = int(left_x), int(left_y), int(right_x), int(right_y)

        if left_x == right_x or left_y == right_y:
            print('Points aligned')
            continue

        area = (abs(left_x-right_x)+1) * (abs(left_y-right_y)+1)
        if area > max_area:
            print('Found new max; ', area)
            max_area = area
    print(max_area)