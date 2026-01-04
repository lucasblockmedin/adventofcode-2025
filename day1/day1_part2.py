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
        loops = quantity // wheel_size
        remainder = quantity % wheel_size
        if direction == 'L':
            prev = curr
            curr = (curr - quantity) % wheel_size
            if curr > prev and prev != 0:
                loops +=1
        elif direction == 'R':
            prev = curr
            curr = (curr + quantity) % wheel_size
            if curr < prev and curr != 0:
                loops +=1
        if curr == 0:
            loops += 1
        print(f'We went {direction} for value {quantity} so we have to count {loops} passes by 0')
        print(f'The current value is {curr}')
        times_at_0 += loops

print('Total:', times_at_0)