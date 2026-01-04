with open('day5_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    split_element = ''
    index = data.index(split_element)
    first_part = data[:index]
    print(first_part)
    rows = []
    for elem in first_part:
        left, right = elem.split('-')
        rows.append([int(left), int(right)])
    print(rows)
    rows.sort(key=lambda x: x[0])
    print(rows)
    i = 1
    while i < len(rows):
        current_left = rows[i][0]
        current_right = rows[i][1]
        print('Current left, ', current_left)
        print('Current right, ', current_right)
        previous_right = rows[i-1][1]
        print('Previous right, ', previous_right)
        if current_left <= previous_right:
            # We combine the current range and the previous range
            rows[i-1][1] = max(current_right, previous_right)
            rows.pop(i)
            # Don't increment i because the next element is now at position i
        else:
            # Only increment if we didn't merge
            i += 1
    print(rows)
    total = 0
    for row in rows:
        total += row[1] - row[0] + 1
    print(total)
