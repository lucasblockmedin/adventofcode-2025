curr = 50
wheel_size = 100
times_at_0 = 0
with open('day1_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    # remove the last element of the list
    data.pop()
    print(data)
    for elem in data:
        direction = elem[0]
        quantity = int(elem[1:])
        curr = (curr - quantity) % wheel_size if direction == 'L' else (curr + quantity) % wheel_size
        print(curr)
        if curr == 0:
            times_at_0 += 1

print('Total:', times_at_0)
