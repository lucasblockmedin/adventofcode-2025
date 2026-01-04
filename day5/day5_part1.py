with open('day5_input.txt') as f:
    # read the file
    data = f.read()
    # split the data into a list
    data = data.split('\n')
    print(data)
    split_element = ''
    index = data.index(split_element)
    first_part = data[:index]
    second_part = data[index+1:]
    print(first_part)
    print(second_part)
    res = 0
    final_list = []
    for line in first_part:
        left, right = line.split('-')
        final_list.append(int(left))
        final_list.append(int(right))
    print(final_list)
    final_list = sorted(final_list)
    print(final_list)
    total = 0
    for i in range(len(final_list)-1):
        total += final_list[i+1] - final_list[i]
        print('Total, ', total)
    
    
        






